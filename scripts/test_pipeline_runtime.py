"""Offline runtime-lock, candidate-isolation, and fail-closed regression checks."""

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

import pipeline_lock


spec = importlib.util.spec_from_file_location(
    "pipeline",
    Path(__file__).with_name("knowledge-pipeline.py"),
)
pipeline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pipeline)


class RuntimeSafetyTests(unittest.TestCase):

    def test_nested_lock_preserves_exclusion_and_rejects_forged_fd(self):
        with tempfile.TemporaryDirectory() as tmp:
            lock = Path(tmp) / "writer.lock"

            code = (
                "import pipeline_lock; "
                "from pathlib import Path; "
                f"pipeline_lock.LOCK_PATH=Path({str(lock)!r}); "
                "raise SystemExit("
                "pipeline_lock.run_locked(lambda: 0)"
                ")"
            )

            with (
                patch.object(pipeline_lock, "LOCK_PATH", lock),
                pipeline_lock.shared_lock() as fd,
            ):
                env = dict(os.environ)
                env["PYTHONPATH"] = str(Path(__file__).parent)
                env[pipeline_lock.FD_ENV] = str(fd)

                inherited = subprocess.run(
                    [sys.executable, "-c", code],
                    env=env,
                    pass_fds=(fd,),
                    capture_output=True,
                )
                self.assertEqual(inherited.returncode, 0)

                forged = dict(env)
                forged[pipeline_lock.FD_ENV] = "999999"

                outsider = subprocess.run(
                    [sys.executable, "-c", code],
                    env=forged,
                    capture_output=True,
                )
                self.assertEqual(outsider.returncode, 75)

            released = subprocess.run(
                [sys.executable, "-c", code],
                env=forged,
                capture_output=True,
            )
            self.assertEqual(released.returncode, 0)

    def test_run_steps_passes_inherited_lock_fd(self):
        calls = []

        def execute(command, **kwargs):
            calls.append((command, kwargs))
            return SimpleNamespace(
                returncode=0,
                stdout=b"",
                stderr=b"",
            )

        with patch.object(
            pipeline,
            "inherited_lock_fd",
            return_value=123,
        ):
            result = pipeline.run_steps(
                [("step", ["command"])],
                execute=execute,
            )

        self.assertEqual(
            result,
            [{"step": "step", "exit_code": 0}],
        )
        self.assertEqual(calls[0][1]["pass_fds"], (123,))

    def test_missing_web_dependencies_are_restored_notified_or_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            web = Path(tmp)
            calls, notes = [], []

            def ok(command, **kwargs):
                calls.append(command)
                return SimpleNamespace(returncode=0)

            def lost(command, **kwargs):
                raise FileNotFoundError("npm")

            with patch.object(pipeline, "WEB", web):
                self.assertEqual(
                    pipeline.ensure_web_dependencies(execute=ok, notify=notes.append),
                    [{"step": "Prepare:web-dependencies", "exit_code": 0,
                      "diagnostic": "DEPENDENCIES_RESTORED",
                      "node_modules_dir_present": False}],
                )
                self.assertEqual(calls[0][1:], ["ci", "--no-audit", "--no-fund"])
                self.assertIn("자동 복구했습니다", notes[0])
                self.assertIn("전체 유실", notes[0])

                failed = pipeline.ensure_web_dependencies(execute=lost, notify=notes.append)
                self.assertEqual(failed[0]["diagnostic"], "DEPENDENCY_RESTORE_FAILED")
                self.assertIn("복구 실패", notes[1])

                (web / "node_modules/tsx").mkdir(parents=True)
                (web / "node_modules/tsx/package.json").write_text("{}")
                calls.clear()
                notes.clear()
                self.assertEqual(
                    pipeline.ensure_web_dependencies(execute=ok, notify=notes.append), [])
                self.assertEqual((calls, notes), ([], []))

    def test_failure_stops_next_step_and_redacts_output(self):
        calls = []

        def execute(command, **kwargs):
            calls.append(command)
            return SimpleNamespace(
                returncode=1,
                stdout=b"private source text",
                stderr=b"MODEL_CACHE_UNAVAILABLE token=do-not-copy",
            )

        result = pipeline.run_steps(
            [
                ("Generate:embeddings", ["embed"]),
                ("Publish:policy-candidate", ["publish"]),
            ],
            execute=execute,
        )

        self.assertEqual(len(calls), 1)
        self.assertEqual(
            result,
            [{
                "step": "Generate:embeddings",
                "exit_code": 1,
                "diagnostic": "MODEL_CACHE_UNAVAILABLE",
            }],
        )
        serialized = json.dumps(result)
        self.assertNotIn("do-not-copy", serialized)
        self.assertNotIn("private source text", serialized)

    def test_unique_candidate_root_uses_three_stage_publication(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root = base / "source"
            web = base / "web"
            candidates_root = base / "candidates"

            root.mkdir()
            web.mkdir()

            created = []
            publication_runs = []

            def fake_run_steps(items):
                names = [name for name, _ in items]

                if any(name.startswith("Publish:") for name in names):
                    publication_runs.append(names)

                    reconcile = [
                        cmd for name, cmd in items
                        if name == "Publish:reconcile-candidates"
                    ]
                    if reconcile:
                        target = Path(reconcile[0][-1])
                        target.mkdir(parents=True)
                        (target / "retained").write_text(
                            "original",
                            encoding="utf-8",
                        )
                        created.append(target)

                return [
                    {"step": name, "exit_code": 0}
                    for name, _ in items
                ]

            with (
                patch.object(pipeline, "ROOT", root),
                patch.object(pipeline, "WEB", web),
                patch.object(
                    pipeline_lock,
                    "LOCK_PATH",
                    root / ".ua/knowledge-pipeline.lock",
                ),
                patch.object(
                    pipeline,
                    "shared_lock",
                    pipeline_lock.shared_lock,
                ),
                patch.object(
                    pipeline.subprocess,
                    "run",
                    return_value=SimpleNamespace(
                        returncode=1,
                        stdout="",
                    ),
                ),
                patch.object(
                    pipeline,
                    "run_steps",
                    side_effect=fake_run_steps,
                ),
            ):
                for _ in range(2):
                    with patch(
                        "sys.argv",
                        [
                            "pipeline",
                            "--validate-existing",
                            "--candidate-root",
                            str(candidates_root),
                        ],
                    ):
                        self.assertEqual(pipeline.main(), 0)

            self.assertEqual(len(created), 2)
            self.assertNotEqual(created[0], created[1])

            expected_publication = [
                "Publish:policy-candidate",
                "Publish:version-candidate",
                "Publish:reconcile-candidates",
                "Publish:derived-projection",
            ]

            self.assertEqual(
                publication_runs,
                [expected_publication, expected_publication],
            )

            self.assertEqual(
                (created[0] / "retained").read_text(),
                "original",
            )

    def test_select_steps_fails_closed_when_contract_missing(self):
        plan = [
            ("Validate:all", ["validate"]),
            ("Publish:policy-candidate", ["policy"]),
        ]

        with self.assertRaises(ValueError):
            pipeline.select_steps(
                plan,
                [
                    "Publish:policy-candidate",
                    "Publish:version-candidate",
                    "Publish:reconcile-candidates",
                ],
            )


    def test_writer_entrypoints_are_lock_wired(self):
        scripts = Path(__file__).parent

        shell_writers = [
            "daily-ingest-claude.sh",
            "fetch-inbox.sh",
        ]
        for name in shell_writers:
            body = (scripts / name).read_text()
            self.assertIn("--check-inherited", body, name)
            self.assertIn("with-pipeline-lock.py", body, name)

        python_writers = [
            "apply-kinetic-rules.py",
            "build-canonical-graph.py",
            "embed-docs.py",
            "extract-knowledge-graph.py",
        ]
        for name in python_writers:
            body = (scripts / name).read_text()
            self.assertIn("from pipeline_lock import run_locked", body, name)

        ai_control = (scripts / "ai-control.sh").read_text()
        self.assertIn("--check-inherited", ai_control)
        self.assertNotIn("PIPELINE_LOCK_HELD", ai_control)


if __name__ == "__main__":
    unittest.main()

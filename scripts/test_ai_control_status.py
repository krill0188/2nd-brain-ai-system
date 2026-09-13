"""Launchd inventory fixtures: idle-loaded is not absent and logs remain unread."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('status', Path(__file__).with_name('ai-control-status.py'))
status = importlib.util.module_from_spec(spec)
spec.loader.exec_module(status)


class StatusTests(unittest.TestCase):
    def test_idle_running_and_absent(self):
        jobs = status.loaded_jobs('PID Status Label\n- 0 ai.2nd.daily-ingest\n123 7 ai.2nd.weekly-lint\n- 0 unrelated\n')
        self.assertEqual(jobs['ai.2nd.daily-ingest'], ('-', '0'))
        self.assertEqual(jobs['ai.2nd.weekly-lint'], ('123', '7'))
        self.assertNotIn('ai.2nd.weekly-summary', jobs)
        self.assertEqual(len(jobs), 2)

    def test_log_content_not_read_and_schedule(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'log'
            path.write_text('SENSITIVE-LOG-CONTENT')
            with patch.object(Path, 'read_text', side_effect=AssertionError('must not read')):
                self.assertNotEqual(status.latest_log({'StandardOutPath': str(path)}), 'unknown')
        self.assertEqual(status.schedule({'StartCalendarInterval': {'Weekday': 1, 'Hour': 5, 'Minute': 30}}), '05:30 Weekday=1')


if __name__ == '__main__':
    unittest.main()

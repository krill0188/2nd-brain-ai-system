"""paper_claims_lib.py — 논문 전문 claim 판정 로직(코드가 판정한다).

원본: ~/projectm/hw-collection/20261019/papers-ontology/pipeline.py (일회성 작업 폴더). 일일 파이프라인이 날짜가 박힌 임시 폴더에
의존하지 않도록 판정에 필요한 순수 함수만 그대로 옮겼다. **동작은 원본과 동일해야 한다** — 판정 규칙을 바꾸면 기존 검증 claim(253건)의
의미가 달라지므로, test_paper_claims_lib.py의 회귀 시험(기존 claim 파일 재판정 100% 일치)이 이를 지킨다.

설계: drone-wiki-web/docs/paper-fulltext-pipeline-design.md §4.3
판정 규칙
  1) quote(공백·합자·유니코드 대시 정규화 후)가 원문 텍스트에 그대로 있어야 함 (길이 15~400자)
  2) value에 들어있는 숫자가 모두 quote 안에 있어야 함 (표 값은 quote 안에 같은 숫자가 있어야 통과)
  3) subject/attribute/conditions/locator 비어 있으면 탈락 (조건 없는 일반화 금지)
모델 출력은 후보일 뿐이며 통과 여부는 항상 이 모듈이 결정한다.
"""
import re


def norm(s: str) -> str:
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("ﬀ", "ff").replace("ﬃ", "ffi").replace("ﬄ", "ffl")
    s = s.replace("−", "-").replace("–", "-").replace("—", "-").replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", "", s).lower()


def nums(s: str):
    return re.findall(r"\d+(?:\.\d+)?", str(s))


def check(c, nt):
    """후보 claim 하나를 판정한다. nt는 norm()을 거친 원문 전체. 통과면 None, 탈락이면 사유 문자열."""
    q = c.get("quote", "")
    if not (15 <= len(q) <= 400):
        return "quote 길이 15~400자 아님"
    for k in ("subject", "attribute", "conditions", "locator", "value"):
        if not str(c.get(k, "")).strip():
            return f"{k} 비어 있음"
    if norm(q) not in nt:
        return "quote가 원문에 없음"
    nq = norm(q)
    miss = [v for v in nums(c["value"]) if v not in nq]
    if miss:
        return f"value 숫자 {miss}가 quote에 없음"
    return None


def judge(candidates, text):
    """후보 목록을 원문 text로 판정해 (통과 목록, 탈락 목록[_why 포함])을 돌려준다. 입력 순서를 보존한다."""
    nt = norm(text)
    good, bad = [], []
    for c in candidates:
        why = check(c, nt)
        (bad if why else good).append({**c, "_why": why} if why else c)
    return good, bad


MODEL_RE = re.compile(r"model assumption|assumed|assumption|we assume|assume[sd]?\b|fitted|fit coefficient|identified|nominal model|design parameter|parameter set|analytical model|theoretical", re.I)
SIM_RE = re.compile(r"simulat|numerical|cfd\b|matlab|gazebo|isaac|monte carlo|synthetic", re.I)
CITED_RE = re.compile(r"cited from|secondary data|reported by \w+ et al|from \[\d+\]|as reported in", re.I)


def evidence_kind(c):
    """증거 종류를 코드가 판정(조건·인용 문구 키워드). measurement로 단정하지 않고 'reported'(논문 보고값)를 기본으로 둔다.
    model-assumption/simulation/cited-secondary는 설계 상수 보정에 직접 쓰지 않는 값."""
    t = f"{c.get('conditions','')} {c.get('quote','')} {c.get('attribute','')}"
    if CITED_RE.search(t):
        return "cited-secondary"
    if MODEL_RE.search(t):
        return "model-assumption"
    if SIM_RE.search(t):
        return "simulation"
    return "reported"

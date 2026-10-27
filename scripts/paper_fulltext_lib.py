"""paper_fulltext_lib.py — 논문 전문에서 claim 후보를 만드는 순수 함수 모음(텍스트 추출·청킹·응답 파싱·프롬프트).

설계: drone-wiki-web/docs/paper-fulltext-pipeline-design.md §4.2~4.4.
이 모듈은 모델을 부르지 않는다(호출은 드라이버가 주입). 판정은 paper_claims_lib(코드)가 한다.
PDF 추출은 PyMuPDF(fitz)를 쓰며 ~/2nd/.venv 에서만 설치돼 있다 — 호출부는 반드시 그 인터프리터로 실행한다.
"""
import json
import re

# 수치가 있는 서술 문장만 후보 대상으로 삼는다(호출량 절감 + 인용문이 실제 수치 문장이 되게 함).
NUM_SENT = re.compile(r"\d")
UNIT = re.compile(r"(?:%|\bdB\b|\bkg\b|\bg\b|\bW\b|\bV\b|\bA\b|\bHz\b|\bkHz\b|\bMHz\b|\bGHz\b|\bms\b|\bm/s\b|\bkm\b|\bcm\b|\bmm\b|\bmAh\b|\bWh\b|\bmin\b|°|\bdeg\b|\bN\b|\brad\b|\bfps\b|\bTOPS\b|\bMB\b|\bGB\b|\bs\b|\bm\b)")
REF_HEAD = re.compile(r"^\s*(?:\d+\.?\s*)?(?:references|bibliography|참고문헌)\s*$", re.I | re.M)


SOFT_HYPHEN_BREAK = re.compile(r"-\n(?=[a-z])")
# 모델이 일반 하이픈 대신 쓰는 유니코드 하이픈류(U+2010 하이픈, U+2011 비분리 하이픈, U+2012 숫자 대시)와 비분리 공백
QUOTE_FIX = str.maketrans({"\u2010": "-", "\u2011": "-", "\u2012": "-", "\u00a0": " "})


def canonicalize(text):
    """판정·청킹·저장이 **같은 텍스트**를 보게 하는 정본화. 줄 끝 하이픈 분절('Com-\\npared')을 복원한다.
    실측 결함(2026-10-27 파일럿): 청크에서만 복원하고 판정 텍스트는 복원하지 않아, 모델이 복사한 정상 인용문이 거짓 탈락했다.
    알려진 한계: 줄 끝에서 끊긴 진짜 복합어('multi-\\nobjective')도 이어 붙는다 — 판정은 이 정본 텍스트 기준이며 PDF 표시와 드물게 다를 수 있다."""
    return SOFT_HYPHEN_BREAK.sub("", text)


def clean_candidate(c):
    """후보의 quote에서 모델이 바꿔 쓴 유니코드 하이픈·NBSP만 일반 문자로 되돌린다(다른 필드·내용은 건드리지 않는다)."""
    q = c.get("quote")
    return {**c, "quote": q.translate(QUOTE_FIX)} if isinstance(q, str) else c


def extract_pages(pdf_path):
    """PDF → 페이지별 정본 텍스트 목록. fitz가 없으면 ImportError(호출부가 진단 코드로 처리)."""
    import fitz
    with fitz.open(pdf_path) as d:
        return [canonicalize(p.get_text()) for p in d]


def strip_references(pages):
    """참고문헌 절 이후를 버린다. 뒤쪽 45%에서 마지막 'References' 제목을 찾고, 없으면 그대로 둔다."""
    n = len(pages)
    for i in range(n - 1, int(n * 0.55) - 1, -1):
        m = REF_HEAD.search(pages[i])
        if m:
            return pages[:i] + [pages[i][: m.start()]]
    return pages


def numeric_sentences(pages, min_len=40, max_len=600):
    """수치가 든 문장을 (페이지번호(1부터), 문장) 목록으로. 줄바꿈·하이픈 분절을 먼저 이어 붙인다."""
    out = []
    for pi, text in enumerate(pages, 1):
        t = re.sub(r"-\n(?=[a-z])", "", text)            # 줄 끝 하이픈 분절 복원
        t = re.sub(r"\s*\n\s*", " ", t)
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(\[])", t):
            s = s.strip()
            if min_len <= len(s) <= max_len and NUM_SENT.search(s) and UNIT.search(s):
                out.append((pi, s))
    return out


def make_chunks(sentences, max_chars=5500, max_chunks=4, skip_front=0.08):
    """수치 문장을 청크로 묶는다. 앞부분(제목·초록 영역)은 건너뛰고, 청크가 max_chunks를 넘으면 문서 전반에서 균등하게 고른다."""
    sents = sentences[int(len(sentences) * skip_front):]
    chunks, cur, size = [], [], 0
    for pi, s in sents:
        if size + len(s) > max_chars and cur:
            chunks.append(cur); cur, size = [], 0
        cur.append((pi, s)); size += len(s) + 1
    if cur:
        chunks.append(cur)
    if len(chunks) > max_chunks:                          # 균등 선택(앞·뒤 편중 방지)
        step = len(chunks) / max_chunks
        chunks = [chunks[int(i * step)] for i in range(max_chunks)]
    return chunks


PROMPT = (
    "아래는 논문 본문에서 수치가 든 문장만 모은 발췌다. 여기서 **연구 결과·측정값·사양을 직접 말하는 사실 주장**만 뽑아 JSON 배열로만 답하라. "
    '각 항목: {"subject":대상,"attribute":속성,"value":숫자 문자열,"unit":단위,"conditions":측정·실험 조건(기체·부하·환경·데이터셋·방법 등),'
    '"quote":발췌에서 **글자 그대로 복사한 문장 일부(15~400자, 값의 숫자를 포함)**}. '
    "항목은 **최대 6개**, quote는 값이 든 부분만 짧게(200자 이내)로 쓴다. 배경 설명·일반론·다른 논문 인용값·가정값은 제외한다. 조건을 알 수 없는 주장은 항목을 만들지 않는다. 발췌에 없는 수치는 만들지 않는다. 없으면 []. 설명 금지."
)
JUDGE = (
    "너는 엄격한 검수자다. 인용문과 주장을 보고, 인용문이 그 대상의 그 속성이 그 값이라고 **직접·유일하게** 말하고 있고 "
    "연구 결과·사양(배경·동기·일반론 아님)일 때만 OK, 아니면 NO 한 단어로만 답하라. 인용문에 비슷한 수치가 여러 개라 어느 것인지 모호하면 NO."
)


def chunk_prompt(chunk):
    return PROMPT + "\n\n[발췌]\n" + "\n".join(s for _, s in chunk)


def parse_candidates_ex(raw):
    """모델 응답에서 후보 목록을 꺼낸다. 반환: (항목 목록, 잘림 여부). 완결된 항목이 하나도 없으면 ValueError.

    실측 결함(2026-10-27 파일럿): 모델 응답이 중간에 잘려 ']'가 없는 경우가 흔한데, 배열 전체를 버리면 수율이 왜곡된다.
    그래서 정상 배열이 아니면 첫 '[' 뒤에서 객체를 하나씩 읽어 **완결된 것만** 살리고 잘린 마지막 항목은 버린다.
    """
    s = raw or ""
    m = re.search(r"\[.*\]", s, re.S)
    if m:
        try:
            arr = json.loads(m.group(0))
            if isinstance(arr, list):
                return [c for c in arr if isinstance(c, dict)], False
        except json.JSONDecodeError:
            pass                                          # 아래 복구 경로로
    i = s.find("[")
    if i < 0:
        raise ValueError("JSON 배열 없음")
    dec, pos, out = json.JSONDecoder(), i + 1, []
    while True:
        j = s.find("{", pos)
        if j < 0:
            break
        try:
            obj, end = dec.raw_decode(s, j)
        except json.JSONDecodeError:
            break                                         # 잘린 마지막 항목
        if isinstance(obj, dict):
            out.append(obj)
        pos = end
    if not out:
        raise ValueError("완결된 항목 없음(응답 잘림 또는 형식 오류)")
    return out, True


def parse_candidates(raw):
    """parse_candidates_ex의 항목만 돌려주는 단축형."""
    return parse_candidates_ex(raw)[0]


def locate(chunk, quote):
    """인용문이 속한 페이지를 코드가 정한다(모델이 쓴 locator를 믿지 않는다). 못 찾으면 청크의 첫 페이지."""
    def n(x): return re.sub(r"\s+", "", x).lower()
    nq = n(quote)
    for pi, s in chunk:
        if nq and nq in n(s):
            return f"p.{pi}"
    return f"p.{chunk[0][0]}"


def judge_prompt(c):
    return f"인용문: {c.get('quote')}\n대상: {c.get('subject')}\n속성: {c.get('attribute')}\n값: {c.get('value')} {c.get('unit', '')}"

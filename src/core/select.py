from __future__ import annotations
from difflib import SequenceMatcher
from .teach import normalize

# Simple, fast selector: exact/substring/fuzzy; returns top-k overrides.
def sim(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()

def select_overrides(user_text: str, overrides: list[dict], k: int = 3) -> list[dict]:
    qn = normalize(user_text)
    scored = []
    for it in overrides:
        q = it.get("q", "")
        if not q:
            continue
        score = 0.0
        if qn == q:
            score = 1.5
        elif q in qn or qn in q:
            score = 1.1
        else:
            score = sim(qn, q)  # 0..1
        if score >= 0.65:  # threshold
            scored.append((score, it))
    scored.sort(key=lambda x: x[0], reverse=True)
    seen = set()
    picked = []
    for s, it in scored:
        if it["q"] in seen:
            continue
        picked.append(it)
        seen.add(it["q"])
        if len(picked) == k:
            break
    return picked

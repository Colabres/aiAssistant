from __future__ import annotations
import json
import re
from pathlib import Path

MEM = Path(__file__).resolve().parents[2] / "memory" / "memory.json"

def load_mem():
    if MEM.exists():
        return json.loads(MEM.read_text(encoding="utf-8"))
    return {"persona": {}, "qa_overrides": []}

def save_mem(m):
    MEM.write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding="utf-8")

def normalize(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[?!.,:;()\[\]\"'«»]", "", s)
    s = re.sub(r"\s+", " ", s)
    return s

def teach(q: str, a: str):
    m = load_mem()
    qn = normalize(q)
    for item in m["qa_overrides"]:
        if item.get("q") == qn:
            item["a"] = a
            save_mem(m)
            return
    m["qa_overrides"].append({"q": qn, "a": a})
    save_mem(m)

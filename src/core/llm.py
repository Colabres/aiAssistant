# Optional llama.cpp wrapper
from __future__ import annotations
from pathlib import Path

try:
    from llama_cpp import Llama
except Exception as e:
    Llama = None

from .teach import load_mem

CFG = Path(__file__).resolve().parents[2] / "config" / "config.toml"
try:
    from tomllib import loads as toml_loads  # py311
except Exception:
    import tomli as toml
    def toml_loads(x): return toml.loads(x)

def _load_cfg():
    if CFG.exists():
        return toml_loads(CFG.read_text(encoding="utf-8"))
    return {}

_cfg = _load_cfg()
_model_path = (_cfg.get("model") or {}).get("path", "")

_have_llm = Llama is not None and _model_path

if _have_llm:
    llm = Llama(
        model_path=_model_path,
        n_gpu_layers=-1,
        n_ctx=4096
    )
else:
    llm = None

have_llm = bool(llm)

def chat(system_prompt: str, user_text: str, temperature=0.6, top_p=0.9, max_tokens=160) -> str:
    if not have_llm:
        raise RuntimeError("LLM not available (install llama-cpp-python and set config/model/path)")
    out = llm.create_chat_completion(
        messages=[
            {"role":"system","content":system_prompt},
            {"role":"user","content":user_text}
        ],
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens
    )
    return out["choices"][0]["message"]["content"].strip()

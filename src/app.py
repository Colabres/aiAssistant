from __future__ import annotations
import argparse
import sys
from pathlib import Path
import json
from .core.teach import load_mem, teach
from .core.select import select_overrides
from .core.prompt import build_system_prompt

try:
    from tomllib import loads as toml_loads  # py311+
except Exception:
    import tomli as toml
    def toml_loads(x): return toml.loads(x)

try:
    from .core.llm import chat as llm_chat, have_llm
except Exception:
    have_llm = False
    def llm_chat(*args, **kwargs):
        raise RuntimeError("LLM not available. Install llama-cpp-python and set model path in config.")

CFG_PATH = Path(__file__).resolve().parents[1] / "config" / "config.toml"
MEM_PATH = Path(__file__).resolve().parents[1] / "memory" / "memory.json"

def load_cfg():
    if CFG_PATH.exists():
        return toml_loads(CFG_PATH.read_text(encoding="utf-8"))
    return {}

def parse_teach(line: str):
    # format: teach: вопрос || ответ
    try:
        _, rest = line.split(":", 1)
        q, a = rest.split("||", 1)
        return q.strip(), a.strip()
    except ValueError:
        return None, None

def main():
    ap = argparse.ArgumentParser(description="alexa-lite CLI")
    ap.add_argument("--mode", default="cool", help="cool | kid")
    args = ap.parse_args()

    cfg = load_cfg()
    mode_cfg = cfg.get("mode", {}).get(args.mode, {})
    system_prompt = mode_cfg.get("system_prompt", "Ты — голосовой ассистент.")
    temperature = float(mode_cfg.get("temperature", 0.6))
    top_p = float(mode_cfg.get("top_p", 0.9))
    max_tokens = int(mode_cfg.get("max_tokens", 160))

    print(f"[aiAssistant] mode={args.mode}  llm={'on' if have_llm else 'off'}")
    print("Type your message. Use 'teach: вопрос || ответ' to add an override. Ctrl+C to exit.\n")

    session_summary = ""

    while True:
        try:
            user = input("you> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nbye.")
            break

        if not user:
            continue

        if user.lower().startswith("teach:"):
            q, a = parse_teach(user)
            if not q:
                print("Format: teach: вопрос || ответ")
                continue
            teach(q, a)
            print("ok. saved override.")
            continue

        m = load_mem()
        overrides = m.get("qa_overrides", [])
        persona = m.get("persona", {})

        picked = select_overrides(user, overrides, k=3)
        facts_lines = []
        if persona.get("name"):
            facts_lines.append(f"Имя = {persona['name']}")
        if persona.get("origin"):
            facts_lines.append(f"Происхождение = {persona['origin']}")
        for it in picked:
            facts_lines.append(f"{it['q']} -> {it['a']}")

        sys_prompt = build_system_prompt(system_prompt, facts_lines, session_summary)

        if not have_llm:
            print("\n[debug] SYSTEM PROMPT:\n", sys_prompt)
            print("[debug] (LLM not installed)")
            continue

        reply = llm_chat(
            sys_prompt,
            user,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens
        )
        print("Assistant>", reply)

        
        session_summary = (session_summary + " " + reply).strip()[:160]

if __name__ == "__main__":
    main()

# Alexa-lite (RU-first, local assistant)

A snappy, **Russian-first** local assistant with a two-step pipeline:
1) **Parse → Query** small fact DB (teach/overrides).
2) **Compose prompt** and call LLM (Qwen2.5-7B by default via `llama.cpp`).

This repo is portfolio-ready: clean structure, tests, CI, and a minimal CLI MVP.

## Features
- Fast two-step retrieval: only injects **relevant** facts (top-K).
- **Teach** flow: add “Q→A overrides” or persona facts without training.
- Switchable styles (e.g., *cool* vs *kid*) via config.
- Pluggable STT/TTS modules (stubs included).
- CI: formatting/lint (ruff) + unit tests.

## Quickstart (CLI, text-only)
```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt -r requirements-dev.txt

# (Optional) If you have llama.cpp Python bindings installed and a GGUF model:
# python -m pip install llama-cpp-python
# Place your model under models/llm/ and set path in config/config.toml

python -m src.app --mode cool
```

Type a message; the app will select relevant overrides and (if llama-cpp is installed) query the LLM.
Otherwise it will show what it *would* send.

## Model choice
Default: **Qwen2.5-7B-Instruct (GGUF, Q4_K_M)** via `llama.cpp` (fast, strong RU).
Alternative: **Llama-3.1-8B-Instruct**.

## Teach flow
- Edit `memory/memory.json` or call `POST /teach` in future API.
- CLI demo: type `teach: вопрос || ответ` to add/update an override.

## Project structure
```
alexa-lite/
  src/
    app.py            # CLI runner
    core/
      llm.py          # llama.cpp wrapper (optional)
      teach.py        # load/save memory, teach overrides
      select.py       # fast selector (rules + fuzzy)
      prompt.py       # builds compact system+facts prompt
      stt.py          # stub
      tts.py          # stub
  config/config.toml  # modes, model path, caps
  memory/memory.json  # persona + overrides
  docs/ROADMAP.md
  .github/workflows/ci.yml
  tests/              # unit tests for selector & prompt
```

## License
MIT

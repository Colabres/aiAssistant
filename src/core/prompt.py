from __future__ import annotations

def build_system_prompt(base_prompt: str, facts_lines: list[str], session_summary: str) -> str:
    parts = [base_prompt.strip()]
    if facts_lines:
        parts.append("\nФакты:")
        for line in facts_lines[:3]:
            parts.append(f"- {line}")
    if session_summary:
        parts.append(f"\nКраткое резюме диалога: {session_summary[:160]}")
    return "\n".join(parts)

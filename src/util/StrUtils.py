from __future__ import annotations

# fmt: off

def SanatizeStr(a_string: str) -> str:
    return a_string.lower().replace(" ", "_")
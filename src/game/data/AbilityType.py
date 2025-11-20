from __future__ import annotations

#fmt: off

from dataclasses import dataclass
from typing import Any, Self

@dataclass
class AbilityType:
    id: str
    prereqs: list[str]
    effects: list[str]
from __future__ import annotations

#fmt: off

from dataclasses import dataclass
from abc import ABC

@dataclass
class BaseEffect(ABC):
    id: str
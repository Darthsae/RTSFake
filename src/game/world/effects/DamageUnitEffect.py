from __future__ import annotations

#fmt: off

from dataclasses import dataclass
from .BaseEffect import BaseEffect

@dataclass
class DamageUnitEffect(BaseEffect):
    amount: float
    damageType: str
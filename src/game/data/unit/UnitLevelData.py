from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Self
if TYPE_CHECKING:
    from .UnitSpawnData import UnitSpawnData

@dataclass
class UnitLevelData:
    unitSpawnData: UnitSpawnData

    @classmethod
    def FromDict(cls, a_data: dict[str, Any]) -> Self:
        return cls(
            a_data["unit_id"],
        )

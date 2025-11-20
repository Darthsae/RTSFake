from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ...data.unit.UnitStatSpec import UnitStatSpec
    from ....util.Typing import AnyDict

@dataclass
class UnitStatInstance:
    statID: str
    statMin: int
    statCurrent: int
    statMax: int

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(a_data["stat_id"], a_data["stat_min"], a_data["stat_cur"], a_data["stat_max"])
    
    @classmethod
    def FromSpec(cls, a_spec: UnitStatSpec) -> Self:
        return cls(a_spec.statID, a_spec.statMin, a_spec.statCurrent, a_spec.statMax)

    def ToDict(self) -> AnyDict:
        return {
            "stat_id": self.statID,
            "stat_min": self.statMin,
            "stat_cur": self.statCurrent,
            "stat_max": self.statMax
        }


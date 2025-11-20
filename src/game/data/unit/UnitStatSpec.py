from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from typing import Self, TYPE_CHECKING
if TYPE_CHECKING:
    from ....util.Typing import AnyDict

@dataclass
class UnitStatSpec:
    statID: str
    statMin: int
    statCurrent: int
    statMax: int

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(a_data["stat_id"], a_data["stat_min"], a_data["stat_cur"], a_data["stat_max"])

    def ToDict(self) -> AnyDict:
        return {
            "stat_id": self.statID,
            "stat_min": self.statMin,
            "stat_cur": self.statCurrent,
            "stat_max": self.statMax
        }


from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from enum import StrEnum, auto
from ..unit.UnitStatInstance import UnitStatInstance
from ..data_selection.RangeSelect import RangeSelect
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ....util.Typing import AnyDict

class Presence(StrEnum):
    REQUIRED  = auto()
    OPTIONAL  = auto()
    FORBIDDEN = auto()

@dataclass
class UnitStatInstanceIndividualData:
    id: str
    presence: Presence
    min: RangeSelect[int]
    current: RangeSelect[int]
    max: RangeSelect[int]

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            a_data["id"],
            Presence(a_data["presence"]),
            RangeSelect[int].FromDict(a_data["min"]),
            RangeSelect[int].FromDict(a_data["current"]),
            RangeSelect[int].FromDict(a_data["max"])
        )

    def ToDict(self) -> AnyDict:
        return {
            "id": self.id,
            "presence": str(self.presence),
            "min": self.min.ToDict(),
            "current": self.current.ToDict(),
            "max": self.max.ToDict()
        }

class UnitStatInstancePredicate:
    def __init__(self, a_stats: list[UnitStatInstanceIndividualData]) -> None:
        self.stats = a_stats

    def Validate(self, a_stats: dict[str, UnitStatInstance]) -> bool:
        for stat in self.stats:
            present: bool = stat.id in a_stats
            match stat.presence:
                case Presence.REQUIRED:
                    if not present:
                        return False
                    unitStat: UnitStatInstance = a_stats[stat.id]
                    if not stat.min.Test(unitStat.statMin) or not stat.current.Test(unitStat.statCurrent) or not stat.max.Test(unitStat.statMax):
                        return False
                case Presence.OPTIONAL:
                    if present:
                        unitStat: UnitStatInstance = a_stats[stat.id]
                        if not stat.min.Test(unitStat.statMin) or not stat.current.Test(unitStat.statCurrent) or not stat.max.Test(unitStat.statMax):
                            return False
                case Presence.FORBIDDEN:
                    if present:
                        return False
        return True

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            [UnitStatInstanceIndividualData.FromDict(data) for data in a_data["stats"]]
        )

    def ToDict(self) -> AnyDict:
        return {
            "stats": [stat.ToDict() for stat in self.stats]
        }

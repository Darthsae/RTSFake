from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from enum import StrEnum, auto
from ...data.unit.UnitResourceSpec import UnitResourceSpec
from ..data_selection.RangeSelect import RangeSelect
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ....util.Typing import AnyDict

class Presence(StrEnum):
    REQUIRED  = auto()
    OPTIONAL  = auto()
    FORBIDDEN = auto()

@dataclass
class UnitResourceSpecIndividualData:
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

class UnitResourceSpecPredicate:
    def __init__(self, a_resources: list[UnitResourceSpecIndividualData]) -> None:
        self.resources = a_resources

    def Validate(self, a_resources: dict[str, UnitResourceSpec]) -> bool:
        for resource in self.resources:
            present: bool = resource.id in a_resources
            match resource.presence:
                case Presence.REQUIRED:
                    if not present:
                        return False
                    unitResource: UnitResourceSpec = a_resources[resource.id]
                    if not resource.min.Test(unitResource.resourceMin) or not resource.current.Test(unitResource.resourceCurrent) or not resource.max.Test(unitResource.resourceMax):
                        return False
                case Presence.OPTIONAL:
                    if present:
                        unitResource: UnitResourceSpec = a_resources[resource.id]
                        if not resource.min.Test(unitResource.resourceMin) or not resource.current.Test(unitResource.resourceCurrent) or not resource.max.Test(unitResource.resourceMax):
                            return False
                case Presence.FORBIDDEN:
                    if present:
                        return False
        return True

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            [UnitResourceSpecIndividualData.FromDict(data) for data in a_data["resources"]]
        )

    def ToDict(self) -> AnyDict:
        return {
            "resources": [resource.ToDict() for resource in self.resources]
        }

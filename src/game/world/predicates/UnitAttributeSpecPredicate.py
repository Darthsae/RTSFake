from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from enum import StrEnum, auto
from ...data.unit.UnitAttributeSpec import UnitAttributeSpec
from ..data_selection.RangeSelect import RangeSelect
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ....util.Typing import AnyDict

class Presence(StrEnum):
    REQUIRED  = auto()
    OPTIONAL  = auto()
    FORBIDDEN = auto()

@dataclass
class UnitAttributeSpecIndividualData:
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

class UnitAttributeSpecPredicate:
    def __init__(self, a_attributes: list[UnitAttributeSpecIndividualData]) -> None:
        self.attributes = a_attributes

    def Validate(self, a_attributes: dict[str, UnitAttributeSpec]) -> bool:
        for attribute in self.attributes:
            present: bool = attribute.id in a_attributes
            match attribute.presence:
                case Presence.REQUIRED:
                    if not present:
                        return False
                    unitAttribute: UnitAttributeSpec = a_attributes[attribute.id]
                    if not attribute.min.Test(unitAttribute.attributeMin) or not attribute.current.Test(unitAttribute.attributeCurrent) or not attribute.max.Test(unitAttribute.attributeMax):
                        return False
                case Presence.OPTIONAL:
                    if present:
                        unitAttribute: UnitAttributeSpec = a_attributes[attribute.id]
                        if not attribute.min.Test(unitAttribute.attributeMin) or not attribute.current.Test(unitAttribute.attributeCurrent) or not attribute.max.Test(unitAttribute.attributeMax):
                            return False
                case Presence.FORBIDDEN:
                    if present:
                        return False
        return True

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            [UnitAttributeSpecIndividualData.FromDict(data) for data in a_data["attributes"]]
        )

    def ToDict(self) -> AnyDict:
        return {
            "attributes": [attribute.ToDict() for attribute in self.attributes]
        }

from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ...data.unit.UnitAttributeSpec import UnitAttributeSpec
    from ....util.Typing import AnyDict

@dataclass
class UnitAttributeInstance:
    attributeID: str
    attributeMin: int
    attributeCurrent: int
    attributeMax: int

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(a_data["attribute_id"], a_data["attribute_min"], a_data["attribute_cur"], a_data["attribute_max"])
    
    @classmethod
    def FromSpec(cls, a_spec: UnitAttributeSpec) -> Self:
        return cls(a_spec.attributeID, a_spec.attributeMin, a_spec.attributeCurrent, a_spec.attributeMax)

    def ToDict(self) -> AnyDict:
        return {
            "attribute_id": self.attributeID,
            "attribute_min": self.attributeMin,
            "attribute_cur": self.attributeCurrent,
            "attribute_max": self.attributeMax
        }

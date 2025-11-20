from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from typing import Self, TYPE_CHECKING
if TYPE_CHECKING:
    from ....util.Typing import AnyDict

@dataclass
class UnitAttributeSpec:
    attributeID: str
    attributeMin: int
    attributeCurrent: int
    attributeMax: int

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(a_data["attribute_id"], a_data["attribute_min"], a_data["attribute_cur"], a_data["attribute_max"])

    def ToDict(self) -> AnyDict:
        return {
            "attribute_id": self.attributeID,
            "attribute_min": self.attributeMin,
            "attribute_cur": self.attributeCurrent,
            "attribute_max": self.attributeMax
        }

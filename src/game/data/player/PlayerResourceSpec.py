from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ....util.Typing import AnyDict

@dataclass
class PlayerResourceSpec:
    resourceID: str
    resourceMin: int
    resourceCurrent: int
    resourceMax: int

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(a_data["resource_id"], a_data["resource_min"], a_data["resource_cur"], a_data["resource_max"])
    
    def ToDict(self) -> AnyDict:
        return {
            "resource_id": self.resourceID,
            "resource_min": self.resourceMin,
            "resource_cur": self.resourceCurrent,
            "resource_max": self.resourceMax
        }
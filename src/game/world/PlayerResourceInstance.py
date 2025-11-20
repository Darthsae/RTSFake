from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ..data.player.PlayerResourceSpec import PlayerResourceSpec
    from ...util.Typing import AnyDict

@dataclass
class PlayerResourceInstance:
    resourceID: str
    resourceMin: int
    resourceCurrent: int
    resourceMax: int

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(a_data["resource_id"], a_data["resource_min"], a_data["resource_cur"], a_data["resource_max"])
    
    @classmethod
    def FromSpec(cls, a_spec: PlayerResourceSpec) -> Self:
        return cls(a_spec.resourceID, a_spec.resourceMin, a_spec.resourceCurrent, a_spec.resourceMax)

    def ToDict(self) -> AnyDict:
        return {
            "resource_id": self.resourceID,
            "resource_min": self.resourceMin,
            "resource_cur": self.resourceCurrent,
            "resource_max": self.resourceMax
        }


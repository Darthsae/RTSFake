from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Self

from ....structures.AABB3I import AABB3I
if TYPE_CHECKING:
    from ....util.Typing import AnyDict

@dataclass
class TriggerZoneData:
    id: str
    tags: list[str]
    area: AABB3I
    conditions: list[str]
    effects: list[str]

    @classmethod
    def FromDict(cls, a_data: dict[str, Any]) -> Self:
        return cls(
            a_data["id"],
            a_data["tags"],
            AABB3I.FromList(a_data["area"]),
            a_data["conditions"],
            a_data["effects"]
        )
    
    def ToDict(self) -> AnyDict:
        return {
            "id": self.id,
            "tags": self.tags,
            "area": self.area.ToList(),
            "conditions": self.conditions,
            "effects": self.effects
        }


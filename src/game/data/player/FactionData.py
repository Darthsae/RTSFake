from __future__ import annotations

#fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Self

from .PlayerResourceSpec import PlayerResourceSpec
if TYPE_CHECKING:
    from ....util.Typing import AnyDict

@dataclass
class FactionData:
    id: str
    name: str
    description: str
    icon: str
    resources: list[PlayerResourceSpec]
    techResearch: list[str]

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            a_data["id"],
            a_data["name"],
            a_data["description"],
            a_data["icon"],
            [PlayerResourceSpec.FromDict(data) for data in a_data["resources"]],
            a_data["tech_research"]
        )
    
    def ToDict(self) -> AnyDict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "icon": self.icon,
            "resources": [resource.ToDict() for resource in self.resources],
            "tech_research": self.techResearch
        }
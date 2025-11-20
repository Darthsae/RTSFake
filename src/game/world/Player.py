from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from .PlayerResourceInstance import PlayerResourceInstance
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ...util.Typing import AnyDict

@dataclass
class Player:
    name: str
    icon: str
    resources: list[PlayerResourceInstance]
    techResearchable: list[str]
    techResearched: list[str]

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            a_data["name"],
            a_data["icon"],
            [PlayerResourceInstance.FromDict(resource) for resource in a_data["resources"]],
            a_data["tech_researchable"],
            a_data["tech_researched"]
        )
    
    def ToDict(self) -> AnyDict:
        return {
            "name": self.name,
            "icon": self.icon,
            "resources": [resource.ToDict() for resource in self.resources],
            "tech_researchable": self.techResearchable,
            "tech_researched": self.techResearched
        }
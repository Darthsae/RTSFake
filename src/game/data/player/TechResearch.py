from __future__ import annotations

#fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ....util.Typing import AnyDict

@dataclass
class TechResearch:
    id: str
    name: str
    category: str
    description: str
    icon: str
    prereqs: list[str]
    effects: list[str]

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            a_data["id"],
            a_data["name"],
            a_data["category"],
            a_data["description"],
            a_data["icon"],
            a_data["prereqs"],
            a_data["effects"]
        )
    
    def ToDict(self) -> AnyDict:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "icon": self.icon,
            "prereqs": self.prereqs,
            "effects": self.effects
        }
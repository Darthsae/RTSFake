from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ....util.Typing import AnyDict

@dataclass
class PlayerResourceType:
    id: str
    name: str
    description: str
    icon: str
    

    def __post_init__(self) -> None:
        self.icon

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            a_data["id"], 
            a_data["name"], 
            a_data.get("description", ""), 
            a_data.get("icon", "no_texture")
        )

    def ToDict(self) -> AnyDict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "icon": self.icon
        }
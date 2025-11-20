from __future__ import annotations

#fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from ....util.Typing import AnyDict

@dataclass
class TileType:
    id: str
    name: str
    texture: str
    description: str
    tags: list[str]

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            a_data["id"],
            a_data["name"],
            a_data["texture"],
            a_data["description"],
            a_data["tags"]
        )
    
    def ToDict(self) -> AnyDict:
        return {
            "id": self.id,
            "name": self.name,
            "texture": self.texture,
            "description": self.description,
            "tags": self.tags
        }
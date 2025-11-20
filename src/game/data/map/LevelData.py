from __future__ import annotations

# fmt: off

from dataclasses import dataclass

from .MapData import MapData

from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ....util.Typing import AnyDict

@dataclass
class LevelData:
    id: str
    name: str
    description: str
    maps: dict[str, MapData]

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            a_data["id"],
            a_data["name"],
            a_data["description"],
            {mapName: MapData.FromDict(mapData) for mapName, mapData in a_data["maps"].items()}
        )
    
    def ToDict(self) -> AnyDict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "maps": {mapName: mapData.ToDict() for mapName, mapData in self.maps.items()}
        }

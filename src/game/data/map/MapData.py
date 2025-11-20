from __future__ import annotations

#fmt: off

from dataclasses import dataclass
from ....util.Typing import AnyDict
from .TriggerZoneData import TriggerZoneData
from typing import TYPE_CHECKING, cast, Self
if TYPE_CHECKING:
    ...

@dataclass
class MapData:
    id: str
    name: str
    keys: list[str]
    width: int
    length: int
    height: int
    tiles: list[int]
    triggerZones: dict[str, TriggerZoneData]

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            a_data["id"],
            a_data["name"],
            a_data["keys"],
            a_data["width"],
            a_data["length"],
            a_data["height"],
            a_data["tiles"],
            {triggerZoneName: TriggerZoneData.FromDict(triggerZoneData) for triggerZoneName, triggerZoneData in cast(dict[str, AnyDict], a_data.get("trigger_zones", {})).items()}
        )
    
    def ToDict(self) -> AnyDict:
        return {
            "id": self.id,
            "name": self.name,
            "keys": self.keys,
            "width": self.width,
            "length": self.length,
            "height": self.height,
            "tiles": self.tiles,
            "trigger_zones": {triggerZoneName: triggerZoneData.ToDict() for triggerZoneName, triggerZoneData in self.triggerZones.items()}
        }
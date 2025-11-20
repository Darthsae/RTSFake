from __future__ import annotations

#fmt: off

from ..data.map.MapData import MapData
from ..data.map.LevelData import LevelData
from .Map import Map
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    ...

class World:
    def __init__(self, a_level: LevelData) -> None:
        if ...:
            ...
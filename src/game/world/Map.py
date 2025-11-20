from __future__ import annotations

#fmt: off

from dataclasses import dataclass
from .unit.UnitInstance import UnitInstance
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    ...

@dataclass
class Map:
    levelID: str
    mapID: str
    units: list[UnitInstance]
    
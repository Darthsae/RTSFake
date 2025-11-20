from __future__ import annotations

# fmt: off

from .Registry import Registry
from typing import TYPE_CHECKING, ClassVar
from .unit.UnitAttributeType import UnitAttributeType
from .unit.UnitResourceType import UnitResourceType
from .unit.UnitStatType import UnitStatType
from .unit.UnitType import UnitType
from .AbilityType import AbilityType
from .DamageType import DamageType
from .player.FactionData import FactionData
from .player.PlayerResourceType import PlayerResourceType
from .player.TechCategory import TechCategory
from .player.TechResearch import TechResearch
from .map.LevelData import LevelData
from .map.TileType import TileType

class GameRegistries:
    UnitAttributes:  ClassVar[Registry[UnitAttributeType]]  = Registry[UnitAttributeType]()
    UnitResources:   ClassVar[Registry[UnitResourceType]]   = Registry[UnitResourceType]()
    UnitStats:       ClassVar[Registry[UnitStatType]]       = Registry[UnitStatType]()
    Units:           ClassVar[Registry[UnitType]]           = Registry[UnitType]()
    Abilities:       ClassVar[Registry[AbilityType]]        = Registry[AbilityType]()
    Damages:         ClassVar[Registry[DamageType]]         = Registry[DamageType]()
    Factions:        ClassVar[Registry[FactionData]]        = Registry[FactionData]()
    PlayerResources: ClassVar[Registry[PlayerResourceType]] = Registry[PlayerResourceType]()
    TechCategories:  ClassVar[Registry[TechCategory]]       = Registry[TechCategory]()
    TechResearch:    ClassVar[Registry[TechResearch]]       = Registry[TechResearch]()
    Levels:          ClassVar[Registry[LevelData]]          = Registry[LevelData]()
    Tiles:           ClassVar[Registry[TileType]]           = Registry[TileType]()


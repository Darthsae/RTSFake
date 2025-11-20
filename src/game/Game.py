from __future__ import annotations

# fmt: off

from genericpath import isfile
import json
import os

import pygame

from .data.map.TileType import TileType

from .data.map.LevelData import LevelData

from .data.unit.UnitStatType import UnitStatType

from .data.unit.UnitResourceType import UnitResourceType

from .data.unit.UnitAttributeType import UnitAttributeType

from .data.unit.UnitType import UnitType

from .data.player.FactionData import FactionData

from .data.DamageType import DamageType

from .data.GameRegistries import GameRegistries
from .ModManager import ModManager
from .ConfigManager import ConfigManager
from ..assets.Localization import LocalizationManager
from ..assets.TextureManager import TextureManager
from ..assets.AudioManager import AudioManager
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from os import DirEntry
    from ModManager import ModHeader

class Game:
    def __init__(self) -> None:
        self.registries: GameRegistries = GameRegistries()
        self.modManager: ModManager = ModManager()
        self.configManager: ConfigManager = ConfigManager()
        self.localizationManager: LocalizationManager = LocalizationManager()
        self.textureManager: TextureManager = TextureManager()
        self.audioManager: AudioManager = AudioManager()
    
    def Init(self) -> bool:

        return True
    
    def LoadModContent(self, a_mod: ModHeader) -> None:
        modIDPrefix: str = f"{a_mod.mod.id}:"
        modAssetsPath: str = os.path.join(a_mod.modDir, "assets")
        if os.path.exists(modAssetsPath) and os.path.isdir(modAssetsPath):
            modAudioPath: str = os.path.join(modAssetsPath, "audio")
            if os.path.exists(modAudioPath) and os.path.isdir(modAudioPath):
                paths: list[tuple[str, str]] = [(modAudioPath, modIDPrefix)]
                while len(paths) > 0:
                    directory, pathID = paths.pop()
                    for directoryEntry in os.scandir(directory):
                        if directoryEntry.is_dir():
                            paths.append((directoryEntry.path, f"{pathID}{directoryEntry.name.lower().replace(" ", "_")}/"))
                        elif directoryEntry.is_file():
                            if directoryEntry.name.endswith((".ogg", ".wav")):
                                print(f"Loaded Audio: {directoryEntry.path}")
                                self.audioManager.LoadAudio(f"{pathID}{directoryEntry.name.lower().replace(" ", "_")}", directoryEntry)
                    
            modLangPath: str = os.path.join(modAssetsPath, "lang")
            if os.path.exists(modLangPath) and os.path.isdir(modLangPath):
                for directoryEntry in os.scandir(modLangPath):
                    if directoryEntry.is_file() and directoryEntry.name.endswith(".json"):
                        print(f"Loaded Lang: {directoryEntry.path}")
                        self.localizationManager.LoadLanguageData(directoryEntry)

            modTexturesPath: str = os.path.join(modAssetsPath, "textures")
            if os.path.exists(modTexturesPath) and os.path.isdir(modTexturesPath):
                paths: list[tuple[str, str]] = [(modTexturesPath, modIDPrefix)]
                while len(paths) > 0:
                    directory, pathID = paths.pop()
                    for directoryEntry in os.scandir(directory):
                        if directoryEntry.is_dir():
                            paths.append((directoryEntry.path, f"{pathID}{directoryEntry.name.lower().replace(" ", "_")}/"))
                        elif directoryEntry.is_file():
                            if directoryEntry.name.endswith((".png")):
                                print(f"Loaded Texture: {directoryEntry.path}")
                                self.textureManager.LoadTexture(f"{pathID}{directoryEntry.name.removesuffix(".png").lower().replace(" ", "_")}", directoryEntry)

        modDataPath: str = os.path.join(a_mod.modDir, "data")
        if os.path.exists(modDataPath) and os.path.isdir(modDataPath):
            modAbilitiesDataPath: str = os.path.join(modDataPath, "abilities")
            if os.path.exists(modAbilitiesDataPath) and os.path.isdir(modAbilitiesDataPath):
                ...

            modDamageTypesDataPath: str = os.path.join(modDataPath, "damage_types")
            if os.path.exists(modDamageTypesDataPath) and os.path.isdir(modDamageTypesDataPath):
                for directoryEntry in os.scandir(modDamageTypesDataPath):
                    if os.path.isfile(directoryEntry) and directoryEntry.name.endswith(".json"):
                        with open(directoryEntry) as dataFile:
                            print(f"Loaded Damage Type: {directoryEntry.path}")
                            self.registries.Damages.Register(f"{modIDPrefix}{directoryEntry.name.removesuffix(".json")}", DamageType.FromDict(json.load(dataFile)))

            modFactionsDataPath: str = os.path.join(modDataPath, "factions")
            if os.path.exists(modFactionsDataPath) and os.path.isdir(modFactionsDataPath):
                for directoryEntry in os.scandir(modFactionsDataPath):
                    if os.path.isfile(directoryEntry) and directoryEntry.name.endswith(".json"):
                        with open(directoryEntry) as dataFile:
                            print(f"Loaded Faction: {directoryEntry.path}")
                            self.registries.Factions.Register(f"{modIDPrefix}{directoryEntry.name.removesuffix(".json")}", FactionData.FromDict(json.load(dataFile)))

            modMapsDataPath: str = os.path.join(modDataPath, "maps")
            if os.path.exists(modMapsDataPath) and os.path.isdir(modMapsDataPath):
                for directoryEntry in os.scandir(modMapsDataPath):
                    if directoryEntry.is_dir():
                        modMapDataConfigPath: str = os.path.join(directoryEntry.path, "map.json")
                        if os.path.exists(modMapDataConfigPath) and os.path.isfile(modMapDataConfigPath):
                            with open(modMapDataConfigPath) as mapDataFile:
                                print(f"Loaded Map: {directoryEntry.path}")
                                self.registries.Levels.Register(f"{modIDPrefix}{directoryEntry.name}", LevelData.FromDict(json.load(mapDataFile)))

            mod_DataPath: str = os.path.join(modDataPath, "_")
            if os.path.exists(mod_DataPath) and os.path.isdir(mod_DataPath):
                ...

            mod_DataPath: str = os.path.join(modDataPath, "_")
            if os.path.exists(mod_DataPath) and os.path.isdir(mod_DataPath):
                ...

            modTilesDataPath: str = os.path.join(modDataPath, "tiles")
            if os.path.exists(modTilesDataPath) and os.path.isdir(modTilesDataPath):
                for directoryEntry in os.scandir(modTilesDataPath):
                    if os.path.isfile(directoryEntry) and directoryEntry.name.endswith(".json"):
                        with open(directoryEntry) as dataFile:
                            print(f"Loaded Tile: {directoryEntry.path}")
                            self.registries.Tiles.Register(f"{modIDPrefix}{directoryEntry.name.removesuffix(".json")}", TileType.FromDict(json.load(dataFile)))

            modUnitsDataPath: str = os.path.join(modDataPath, "units")
            if os.path.exists(modUnitsDataPath) and os.path.isdir(modUnitsDataPath):
                modUnitAttributesDataPath: str = os.path.join(modUnitsDataPath, "unit_attributes")
                if os.path.exists(modUnitAttributesDataPath) and os.path.isdir(modUnitAttributesDataPath):
                    for directoryEntry in os.scandir(modUnitAttributesDataPath):
                        if os.path.isfile(directoryEntry) and directoryEntry.name.endswith(".json"):
                            with open(directoryEntry) as dataFile:
                                print(f"Loaded Unit Attribute: {directoryEntry.path}")
                                self.registries.UnitAttributes.Register(f"{modIDPrefix}{directoryEntry.name.removesuffix(".json")}", UnitAttributeType.FromDict(json.load(dataFile)))

                modUnitResourcesDataPath: str = os.path.join(modUnitsDataPath, "unit_resources")
                if os.path.exists(modUnitResourcesDataPath) and os.path.isdir(modUnitResourcesDataPath):
                    for directoryEntry in os.scandir(modUnitResourcesDataPath):
                        if os.path.isfile(directoryEntry) and directoryEntry.name.endswith(".json"):
                            with open(directoryEntry) as dataFile:
                                print(f"Loaded Unit Resource: {directoryEntry.path}")
                                self.registries.UnitResources.Register(f"{modIDPrefix}{directoryEntry.name.removesuffix(".json")}", UnitResourceType.FromDict(json.load(dataFile)))
                                
                modUnitStatsDataPath: str = os.path.join(modUnitsDataPath, "unit_stats")
                if os.path.exists(modUnitStatsDataPath) and os.path.isdir(modUnitStatsDataPath):
                    for directoryEntry in os.scandir(modUnitStatsDataPath):
                        if os.path.isfile(directoryEntry) and directoryEntry.name.endswith(".json"):
                            with open(directoryEntry) as dataFile:
                                print(f"Loaded Unit Stat: {directoryEntry.path}")
                                self.registries.UnitStats.Register(f"{modIDPrefix}{directoryEntry.name.removesuffix(".json")}", UnitStatType.FromDict(json.load(dataFile)))

                for directoryEntry in os.scandir(modUnitsDataPath):
                    if os.path.isfile(directoryEntry) and directoryEntry.name.endswith(".json"):
                        with open(directoryEntry) as dataFile:
                            print(f"Loaded Unit: {directoryEntry.path}")
                            self.registries.Units.Register(f"{modIDPrefix}{directoryEntry.name.removesuffix(".json")}", UnitType.FromDict(json.load(dataFile)))

    def SearchMods(self) -> bool:
        keepers: list[DirEntry[str]] = []
        modsPath: str = os.path.join(os.getcwd(), "mods")
        for directoryEntry in os.scandir(modsPath):
            result = self.modManager.EvaluateModCandidate(directoryEntry)
            if result == 0:
                keepers.append(directoryEntry)
        for kept in keepers:
            header: ModHeader = self.modManager.LoadModHeader(kept)
            
        return True

    def ReloadMods(self) -> bool:
        for modID, (_, modEnabled, modDir) in self.modManager.mods.items():
            if modEnabled:
                # Do an os.walk here.
                ...
        self.modManager.ReloadMods(self)
        return True

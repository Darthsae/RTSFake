from __future__ import annotations

# fmt: off

import os

import yaml
from yaml import loader

from .data.Mod import Mod
from typing import TYPE_CHECKING, NamedTuple
if TYPE_CHECKING:
    from os import DirEntry
    from .Game import Game

class ModHeader(NamedTuple):
    mod: Mod
    enabled: bool
    modDir: str

class ModManager:
    def __init__(self) -> None:
        self.mods: dict[str, ModHeader] = {}

    def EvaluateModCandidate(self, a_dirEntry: DirEntry[str]) -> int:
        if not a_dirEntry.is_dir():
            return -1
        modConfigPath: str = os.path.join(a_dirEntry.path, "mod.yaml")
        if not os.path.exists(modConfigPath):
            return -2
        if not os.path.isfile(modConfigPath):
            return -3
        return 0
    
    def LoadModHeader(self, a_dirEntry: DirEntry[str]) -> ModHeader:
        modConfigPath: str = os.path.join(a_dirEntry.path, "mod.yaml")
        with open(modConfigPath) as modConfigFile:
            self.mods[header.mod.id] = (header := ModHeader(Mod.FromDict(yaml.load(modConfigFile, loader.FullLoader)), False, a_dirEntry.path))
        return header

    def ReloadMods(self, a_game: Game) -> None:
        for modID, (_, modEnabled, modDir) in self.mods.items():
            if modEnabled:
                ...

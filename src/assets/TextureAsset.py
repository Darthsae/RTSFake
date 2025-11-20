from __future__ import annotations

#fmt: off

import pygame
from dataclasses import dataclass
from typing import Self, TYPE_CHECKING
if TYPE_CHECKING:
    from pygame import Surface

@dataclass
class TextureAsset:
    id: str
    name: str
    path: str
    textureSurface: Surface

    @classmethod
    def Load(cls, a_id: str, a_name: str, a_path: str) -> Self:
        return cls(a_id, a_name, a_path, pygame.image.load(a_path))
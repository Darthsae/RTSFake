from __future__ import annotations

# fmt: off

from .TextureAsset import TextureAsset

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from os import DirEntry

class TextureManager:
    def __init__(self) -> None:
        self.textures: dict[str, TextureAsset] = {}

    def LoadTexture(self, a_id: str, a_path: DirEntry[str]) -> bool:
        self.textures[a_id] = TextureAsset.Load(a_id, a_path.name, a_path.path)
        return True
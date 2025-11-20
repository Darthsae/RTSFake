from __future__ import annotations

# fmt: off

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from os import DirEntry
    from .AudioAsset import AudioAsset

class AudioManager:
    def __init__(self) -> None:
        self.audio: dict[str, AudioAsset] = {}

    def LoadAudio(self, a_id: str, a_path: DirEntry[str]) -> bool:
        self.audio[a_id] = AudioAsset.Load(a_id, a_path.name, a_path.path)
        return True


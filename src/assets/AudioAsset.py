from __future__ import annotations

# fmt: off

from pygame import Sound
from dataclasses import dataclass
from typing import Self, TYPE_CHECKING
if TYPE_CHECKING:
    ...

@dataclass
class AudioAsset:
    id: str
    name: str
    path: str
    audioSound: Sound

    @classmethod
    def Load(cls, a_id: str, a_name: str, a_path: str) -> Self:
        return cls(a_id, a_name, a_path, Sound(a_path))


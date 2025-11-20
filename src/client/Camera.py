from __future__ import annotations

# fmt: off

from dataclasses import dataclass

from typing import TYPE_CHECKING

from ..structures.Vec2I import Vec2I
if TYPE_CHECKING:
    ...

@dataclass
class Camera:
    pos: Vec2I
    size: Vec2I
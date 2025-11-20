from __future__ import annotations

#fmt: off

from typing import TYPE_CHECKING
from .Animation import Animation
if TYPE_CHECKING:
    from ..PygameHolder import PygameHolder

class AnimationManager:
    def __init__(self) -> None:
        self.animations: dict[str, Animation] = {}

    def Update(self, a_pygameHolder: PygameHolder) -> None:
        self.animations = {id: anim for id, animation in self.animations.items() if (anim := animation.Update(a_pygameHolder)) != None}
        
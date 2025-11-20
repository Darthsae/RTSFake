from __future__ import annotations

#fmt: off

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Callable
    from ..PygameHolder import PygameHolder
    from .Animation import Animation

type AnimationAction = Callable[[Animation, PygameHolder], None]
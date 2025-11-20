from __future__ import annotations

#fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from .AnimationHooks import AnimationAction
    from .Curves import Curve
    from ..PygameHolder import PygameHolder

@dataclass
class Animation:
    curve: Curve
    onStart: Optional[AnimationAction] = None
    onUpdate: Optional[AnimationAction] = None
    onEnd: Optional[AnimationAction] = None

    def Update(self, a_pygameHolder: PygameHolder) -> Optional[Animation]:
        """
        """
        self.curve.Update(a_pygameHolder.deltaTime)
        if self.onUpdate:
            self.onUpdate(self, a_pygameHolder)
        if self.curve.progress >= 1:
            if self.onEnd:
                self.onEnd(self, a_pygameHolder)
            return None
        return self
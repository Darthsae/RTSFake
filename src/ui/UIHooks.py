from __future__ import annotations

#fmt: off

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Callable
    from .UIManager import UIManager
    from .UIElement import UIElement
    from ..PygameHolder import PygameHolder
    from pygame import Vector2, Surface

type UIElementAction = Callable[[PygameHolder, UIManager, UIElement], None]
type UIElementPredicate = Callable[[PygameHolder, UIManager, UIElement], bool]
type UIElementDrawAction = Callable[[PygameHolder, UIManager, UIElement, Surface], None]
type UIElementMouseAction = Callable[[PygameHolder, UIManager, Vector2, UIElement], None]
type UIElementMousePredicate = Callable[[PygameHolder, UIManager, Vector2, UIElement], bool]
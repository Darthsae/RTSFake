from __future__ import annotations

#fmt: off

import pygame
from pygame import Vector2, Surface, Rect
from .UIInputHolder import UIInputHolder
from ..animation.Curves import Curve
from typing import TYPE_CHECKING, Callable
if TYPE_CHECKING:
    from .UILayer import UILayer
    from .UIElement import UIElement
    from ..PygameHolder import PygameHolder

class UIManager:
    def __init__(self) -> None:
        self.layers: list[UILayer] = []
        self.elements: dict[str, UIElement] = {}
        self.hovered: list[str] = []
        self.updates: dict[str, Callable[[PygameHolder, UIManager], None]] = {}
    
    def Recalculate(self, a_pygameHolder: PygameHolder) -> None:
        [layer.Recalculate(a_pygameHolder, self) for layer in self.layers]

    def Render(self, a_pygameHolder: PygameHolder) -> Surface:
        screen: Rect = a_pygameHolder.screen.get_rect()
        surface: Surface = Surface(a_pygameHolder.screen.size, pygame.SRCALPHA)
        surface.fblits([(layer.Render(a_pygameHolder, self), screen) for layer in self.layers])
        return surface

    def HandleInput(self, a_pygameHolder: PygameHolder, a_mousePos: Vector2, a_button: int) -> bool:
        print(a_mousePos)
        uncaptured: bool = True
        inputHolder: UIInputHolder = UIInputHolder()
        for layer in self.layers:
            if (uncaptured := layer.HandleInput(a_pygameHolder, self, inputHolder, a_mousePos, a_button)):
                break
        [element.HandleMouseExit(a_pygameHolder, self, a_mousePos) for hovered in self.hovered if not (element := self.elements[hovered]).displayRect.contains(a_mousePos) or not element.active]
        return uncaptured
    
    def Update(self, a_pygameHolder: PygameHolder) -> None:
        [update(a_pygameHolder, self) for update in self.updates.values()]
        
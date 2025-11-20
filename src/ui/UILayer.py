from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import pygame
from pygame import Surface, Vector2
if TYPE_CHECKING:
    from .UIManager import UIManager
    from ..PygameHolder import PygameHolder
    from .UIInputHolder import UIInputHolder
    from .UIElement import UIElement

class UILayer:
    def __init__(self, /, a_active: bool = True, a_elements: Optional[list[str]] = None) -> None:
        self.active: bool = a_active
        self.elements: list[str] = [] if a_elements is None else a_elements
    
    def Recalculate(self, a_pygameHolder: PygameHolder, a_uiManager: UIManager) -> None:
        [a_uiManager.elements[element].Recalculate(a_pygameHolder, a_uiManager, Vector2(0, 0)) for element in self.elements]

    def Render(self, a_pygameHolder: PygameHolder, a_uiManager: UIManager) -> Surface:
        surface: Surface = Surface(a_pygameHolder.screen.size, pygame.SRCALPHA)
        if self.active:
            surface.fblits([((element := a_uiManager.elements[elementID]).Render(a_pygameHolder, a_uiManager), element.displayRect) for elementID in self.elements])
        return surface
    
    def HandleInput(self, a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_uiInputHolder: UIInputHolder, a_mousePos: Vector2, a_button: int) -> bool:
        print(a_mousePos)
        for element in self.elements:
            uiElement: UIElement = a_uiManager.elements[element]
            if uiElement.displayRect.collidepoint(a_mousePos) and uiElement.active:
                returnable: bool = False
                match a_button:
                    case 1:
                        if uiElement.HandleLeftMouseDown(a_pygameHolder, a_uiManager, a_mousePos):
                            returnable = True
                    case 2:
                        if uiElement.HandleMiddleMouseDown(a_pygameHolder, a_uiManager, a_mousePos):
                            returnable = True
                    case 3:
                        if uiElement.HandleRightMouseDown(a_pygameHolder, a_uiManager, a_mousePos):
                            returnable = True
                if uiElement.HandleMouse(a_pygameHolder, a_uiManager, a_mousePos):
                    return True
                return returnable
        return False
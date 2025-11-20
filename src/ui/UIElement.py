from __future__ import annotations
from .UIAnchor import UIAnchor
from .UIBorder import UIBorder
import pygame
from pygame import FRect, Vector2, Surface
from .. import Constants
from typing import TYPE_CHECKING, Any, Optional
if TYPE_CHECKING:
    from UIManager import UIManager 
    from ..PygameHolder import PygameHolder
    from .UIHooks import UIElementMousePredicate, UIElementMouseAction, UIElementDrawAction, UIElementAction, UIElementPredicate

class UIElement:
    def __init__(self, 
            a_id: str, /, 
            a_active: bool = True, 
            a_parentAnchor: UIAnchor = UIAnchor.TOP_LEFT, 
            a_childAnchor: UIAnchor = UIAnchor.TOP_LEFT, 
            a_internalRect: Optional[FRect] = None, 
            a_children: Optional[list[str]] = None, 
            a_data: Optional[dict[str, Any]] = None, 
            a_margins: Optional[UIBorder] = None, 
            a_padding: Optional[UIBorder] = None, 
            a_canDraw: Optional[list[tuple[str, UIElementPredicate]]] = None, 
            a_onDraw: Optional[list[tuple[str, UIElementDrawAction]]] = None, 
            a_preRecalculate: Optional[list[tuple[str, UIElementAction]]] = None, 
            a_postRecalculate: Optional[list[tuple[str, UIElementAction]]] = None, 
            a_onLeftMouseDown: Optional[list[tuple[str, UIElementMousePredicate]]] = None, 
            a_onLeftMouseHold: Optional[list[tuple[str, UIElementMousePredicate]]] = None, 
            a_onLeftMouseUp: Optional[list[tuple[str, UIElementMousePredicate]]] = None, 
            a_onMiddleMouseDown: Optional[list[tuple[str, UIElementMousePredicate]]] = None, 
            a_onMiddleMouseHold: Optional[list[tuple[str, UIElementMousePredicate]]] = None, 
            a_onMiddleMouseUp: Optional[list[tuple[str, UIElementMousePredicate]]] = None, 
            a_onRightMouseDown: Optional[list[tuple[str, UIElementMousePredicate]]] = None, 
            a_onRightMouseHold: Optional[list[tuple[str, UIElementMousePredicate]]] = None, 
            a_onRightMouseUp: Optional[list[tuple[str, UIElementMousePredicate]]] = None, 
            a_onMouseEnter: Optional[list[tuple[str, UIElementMousePredicate]]] = None, 
            a_onMouseHover: Optional[list[tuple[str, UIElementMousePredicate]]] = None, 
            a_onMouseExit: Optional[list[tuple[str, UIElementMousePredicate]]] = None) -> None:
        """__summary__

        Args:
            a_id (str): The id of the UI element.
            a_active (bool): ...
            a_parentAnchor (UIAnchor): ...
            a_childAnchor (UIAnchor): ...
            a_internalRect (Optional[FRect]): ...
            a_children (Optional[list[str]]): ...
            a_data (Optional[dict[str, Any]]): ...
            a_margins (Optional[UIBorder]): ...
            a_padding (Optional[UIBorder]): ...
            a_canDraw (Optional[list[tuple[str, UIElementPredicate]]]): ...
            a_onDraw (Optional[list[tuple[str, UIElementDrawAction]]]): ...
            a_preRecalculate (Optional[list[tuple[str, UIElementAction]]]): ...
            a_postRecalculate (Optional[list[tuple[str, UIElementAction]]]): ...
            a_onLeftMouseDown (Optional[list[tuple[str, UIElementMousePredicate]]]): ...
            a_onLeftMouseHold (Optional[list[tuple[str, UIElementMousePredicate]]]): ...
            a_onLeftMouseUp (Optional[list[tuple[str, UIElementMousePredicate]]]): ...
            a_onMiddleMouseDown (Optional[list[tuple[str, UIElementMousePredicate]]]): ...
            a_onMiddleMouseHold (Optional[list[tuple[str, UIElementMousePredicate]]]): ...
            a_onMiddleMouseUp (Optional[list[tuple[str, UIElementMousePredicate]]]): ...
            a_onRightMouseDown (Optional[list[tuple[str, UIElementMousePredicate]]]): ...
            a_onRightMouseHold (Optional[list[tuple[str, UIElementMousePredicate]]]): ...
            a_onRightMouseUp (Optional[list[tuple[str, UIElementMousePredicate]]]): ...
            a_onMouseEnter (Optional[list[tuple[str, UIElementMousePredicate]]]): ...
            a_onMouseHover (Optional[list[tuple[str, UIElementMousePredicate]]]): ...
            a_onMouseExit (Optional[list[tuple[str, UIElementMousePredicate]]]): ...
        """
        self.id: str = a_id
        self.active: bool = a_active
        self.parentAnchor: UIAnchor = a_parentAnchor
        self.childAnchor:  UIAnchor = a_childAnchor
        self.internalRect: FRect = FRect(0, 0, 1, 1) if a_internalRect is None else a_internalRect
        self.displayRect:  FRect = FRect(0, 0, 0, 0)
        self.children: list[str] = [] if a_children is None else a_children
        self.data: dict[str, Any] = {} if a_data is None else a_data

        # Margins (Internal)
        self.margins: UIBorder = UIBorder() if a_margins is None else a_margins

        # Paddings (External)
        self.padding: UIBorder = UIBorder() if a_padding is None else a_padding

        #region Hooks
        self.CanDraw: list[tuple[str, UIElementPredicate]]  = [] if a_canDraw is None else a_canDraw
        self.OnDraw:  list[tuple[str, UIElementDrawAction]] = [] if a_onDraw  is None else a_onDraw

        self.PreRecalculate:  list[tuple[str, UIElementAction]] = [] if a_preRecalculate  is None else a_preRecalculate
        self.PostRecalculate: list[tuple[str, UIElementAction]] = [] if a_postRecalculate is None else a_postRecalculate

        self.OnLeftMouseDown: list[tuple[str, UIElementMousePredicate]] = [] if a_onLeftMouseDown is None else a_onLeftMouseDown
        self.OnLeftMouseHold: list[tuple[str, UIElementMousePredicate]] = [] if a_onLeftMouseHold is None else a_onLeftMouseHold
        self.OnLeftMouseUp:   list[tuple[str, UIElementMousePredicate]] = [] if a_onLeftMouseUp   is None else a_onLeftMouseUp

        self.OnMiddleMouseDown: list[tuple[str, UIElementMousePredicate]] = [] if a_onMiddleMouseDown is None else a_onMiddleMouseDown
        self.OnMiddleMouseHold: list[tuple[str, UIElementMousePredicate]] = [] if a_onMiddleMouseHold is None else a_onMiddleMouseHold
        self.OnMiddleMouseUp:   list[tuple[str, UIElementMousePredicate]] = [] if a_onMiddleMouseUp   is None else a_onMiddleMouseUp

        self.OnRightMouseDown: list[tuple[str, UIElementMousePredicate]] = [] if a_onRightMouseDown is None else a_onRightMouseDown
        self.OnRightMouseHold: list[tuple[str, UIElementMousePredicate]] = [] if a_onRightMouseHold is None else a_onRightMouseHold
        self.OnRightMouseUp:   list[tuple[str, UIElementMousePredicate]] = [] if a_onRightMouseUp   is None else a_onRightMouseUp

        self.OnMouseEnter: list[tuple[str, UIElementMousePredicate]] = [] if a_onMouseEnter is None else a_onMouseEnter
        self.OnMouseHover: list[tuple[str, UIElementMousePredicate]] = [] if a_onMouseHover is None else a_onMouseHover
        self.OnMouseExit:  list[tuple[str, UIElementMousePredicate]] = [] if a_onMouseExit  is None else a_onMouseExit
        #endregion

        self.previousParentAnchor: Vector2 = Vector2(0, 0)

        #self.Can: list[tuple[str, UIElementPredicate]] = []
        #self.On: list[tuple[str, UIElementAction]] = []

    def Recalculate(self, a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_anchorPoint: Vector2) -> None:
        if self.active:
            [recalculate(a_pygameHolder, a_uiManager, self) for (_, recalculate) in self.PreRecalculate]
            self.displayRect = self.internalRect.scale_by(a_pygameHolder.screen.width/Constants.SCREEN_WIDTH, a_pygameHolder.screen.height/Constants.SCREEN_HEIGHT)
            match self.parentAnchor:
                case UIAnchor.TOP_LEFT:
                    self.displayRect.topleft     = Vector2(self.displayRect.topleft) + a_anchorPoint + Vector2(self.padding.left, self.padding.top)
                case UIAnchor.TOP_CENTER:
                    self.displayRect.midtop      = Vector2(self.displayRect.topleft) + a_anchorPoint + Vector2(0, self.padding.top)
                case UIAnchor.TOP_RIGHT:
                    self.displayRect.topright    = Vector2(self.displayRect.topleft) + a_anchorPoint + Vector2(-self.padding.right, self.padding.top)
                case UIAnchor.CENTER_LEFT:
                    self.displayRect.midleft     = Vector2(self.displayRect.topleft) + a_anchorPoint + Vector2(self.padding.left, 0)
                case UIAnchor.CENTER_CENTER:
                    self.displayRect.center      = Vector2(self.displayRect.topleft) + a_anchorPoint
                case UIAnchor.CENTER_RIGHT:
                    self.displayRect.midright    = Vector2(self.displayRect.topleft) + a_anchorPoint + Vector2(-self.padding.right, 0)
                case UIAnchor.BOTTOM_LEFT:
                    self.displayRect.bottomleft  = Vector2(self.displayRect.topleft) + a_anchorPoint + Vector2(self.padding.left, -self.padding.bottom)
                case UIAnchor.BOTTOM_CENTER:
                    self.displayRect.midbottom   = Vector2(self.displayRect.topleft) + a_anchorPoint + Vector2(0, -self.padding.bottom)
                case UIAnchor.BOTTOM_RIGHT:
                    self.displayRect.bottomright = Vector2(self.displayRect.topleft) + a_anchorPoint + Vector2(-self.padding.right, -self.padding.bottom)
            anchorPosition: Vector2
            match self.childAnchor:
                case UIAnchor.TOP_LEFT:
                    anchorPosition = Vector2(self.displayRect.topleft) + Vector2(self.margins.left, self.margins.top)
                case UIAnchor.TOP_CENTER:
                    print(self.displayRect.midtop)
                    anchorPosition = Vector2(self.displayRect.midtop) + Vector2(0, self.margins.top)
                case UIAnchor.TOP_RIGHT:
                    anchorPosition = Vector2(self.displayRect.topright) + Vector2(-self.margins.right, self.margins.top)
                case UIAnchor.CENTER_LEFT:
                    anchorPosition = Vector2(self.displayRect.midleft) + Vector2(self.margins.left, 0)
                case UIAnchor.CENTER_CENTER:
                    anchorPosition = Vector2(self.displayRect.center)
                case UIAnchor.CENTER_RIGHT:
                    anchorPosition = Vector2(self.displayRect.midright) + Vector2(-self.margins.right, 0)
                case UIAnchor.BOTTOM_LEFT:
                    anchorPosition = Vector2(self.displayRect.bottomleft) + Vector2(self.margins.left, -self.margins.bottom)
                case UIAnchor.BOTTOM_CENTER:
                    anchorPosition = Vector2(self.displayRect.midbottom) + Vector2(0, -self.margins.bottom)
                case UIAnchor.BOTTOM_RIGHT:
                    anchorPosition = Vector2(self.displayRect.bottomright) + Vector2(-self.margins.right, -self.margins.bottom)
            [recalculate(a_pygameHolder, a_uiManager, self) for (_, recalculate) in self.PostRecalculate]
            [a_uiManager.elements[id].Recalculate(a_pygameHolder, a_uiManager, anchorPosition) for id in self.children]
    
    def Render(self, a_pygameHolder: PygameHolder, a_uiManager: UIManager) -> Surface:
        toReturn: Surface = Surface(self.displayRect.size, pygame.SRCALPHA)
        if self.active and all([draw(a_pygameHolder, a_uiManager, self) for (_, draw) in self.CanDraw]):
            [draw(a_pygameHolder, a_uiManager, self, toReturn) for (_, draw) in self.OnDraw]
            toReturn.fblits([(a_uiManager.elements[id].Render(a_pygameHolder, a_uiManager), self.displayRect) for id in self.children])
        return toReturn
    
    def HandleLeftMouseDown(self, a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_mousePos: Vector2) -> bool:
        if self.active and all([mouse(a_pygameHolder, a_uiManager, a_mousePos, self) for (_, mouse) in self.OnLeftMouseDown]):
            for child in self.children:
                if a_uiManager.elements[child].HandleLeftMouseDown(a_pygameHolder, a_uiManager, a_mousePos):
                    return True
        return True
    
    def HandleMiddleMouseDown(self, a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_mousePos: Vector2) -> bool:
        if self.active and all([mouse(a_pygameHolder, a_uiManager, a_mousePos, self) for (_, mouse) in self.OnMiddleMouseDown]):
            for child in self.children:
                if a_uiManager.elements[child].HandleMiddleMouseDown(a_pygameHolder, a_uiManager, a_mousePos):
                    return True
        return True
    
    def HandleRightMouseDown(self, a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_mousePos: Vector2) -> bool:
        if self.active and all([mouse(a_pygameHolder, a_uiManager, a_mousePos, self) for (_, mouse) in self.OnRightMouseDown]):
            for child in self.children:
                if a_uiManager.elements[child].HandleRightMouseDown(a_pygameHolder, a_uiManager, a_mousePos):
                    return True
        return True
    
    def HandleMouse(self, a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_mousePos: Vector2) -> bool:
        return (self.HandleMouseHover(a_pygameHolder, a_uiManager, a_mousePos) if self.id in a_uiManager.hovered else self.HandleMouseEnter(a_pygameHolder, a_uiManager, a_mousePos)) if self.active else self.HandleMouseExit(a_pygameHolder, a_uiManager, a_mousePos)
                

    def HandleMouseEnter(self, a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_mousePos: Vector2) -> bool:
        if self.active and all([mouse(a_pygameHolder, a_uiManager, a_mousePos, self) for (_, mouse) in self.OnMouseEnter]):
            for child in self.children:
                if a_uiManager.elements[child].HandleMouseEnter(a_pygameHolder, a_uiManager, a_mousePos):
                    return True
        return True
    
    def HandleMouseHover(self, a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_mousePos: Vector2) -> bool:
        if self.active and all([mouse(a_pygameHolder, a_uiManager, a_mousePos, self) for (_, mouse) in self.OnMouseHover]):
            for child in self.children:
                if a_uiManager.elements[child].HandleMouseHover(a_pygameHolder, a_uiManager, a_mousePos):
                    return True
        return True
    
    def HandleMouseExit(self, a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_mousePos: Vector2) -> bool:
        if self.active and all([mouse(a_pygameHolder, a_uiManager, a_mousePos, self) for (_, mouse) in self.OnMouseExit]):
            for child in self.children:
                if a_uiManager.elements[child].HandleMouseExit(a_pygameHolder, a_uiManager, a_mousePos):
                    return True
        return True
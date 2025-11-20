# fmt: off

import pygame
from pygame import Vector2, FRect, Surface
from src import Constants
from src.animation.AnimationManager import AnimationManager
from src.animation.Animation import Animation
from src.animation.Curves import LinearCurve
from src.PygameHolder import PygameHolder
from src.game.world.Map import Map
from src.client.MapRenderer import MapRenderer
from src.ui import UIManager, UIAnchor, UIBorder, UIElement, UILayer
from src.game.Game import Game
from enum import StrEnum, auto

class Screen(StrEnum):
    MAIN_MENU = auto()
    SETTINGS  = auto()

def RecalculateText(a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_uiElement: UIElement) -> None:
    a_uiElement.data["text_rect"] = (bonk := a_pygameHolder.fonts[60].render(a_uiElement.data["text"], False, Constants.BLACK))
    a_uiElement.data["text_pos"] = ((a_uiElement.displayRect.w - bonk.width) * 0.5, (a_uiElement.displayRect.h - bonk.height) * 0.5)
    
def DrawText(a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_uiElement: UIElement, a_surface: Surface) -> None:
    a_surface.blit(a_uiElement.data["text_rect"], a_uiElement.data["text_pos"])

def DrawFilledRect(a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_uiElement: UIElement, a_surface: Surface) -> None:
    a_surface.fill(a_uiElement.data["rect_color"])

def PlayButton(a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_position: Vector2, a_uiElement: UIElement) -> bool:
    print("Play Pressed")
    return True

def main() -> None:
    pygameHolder: PygameHolder = PygameHolder(Constants.SCREEN_SIZE, 60)
    animationManager: AnimationManager = AnimationManager()
    uiManager: UIManager = UIManager()

    game: Game = Game()

    

    screen: Screen = Screen.MAIN_MENU

    def LeBonk(a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_position: Vector2, a_uiElement: UIElement):
        originalX: float = a_uiElement.internalRect.x
        def LeTonk(a_animation: Animation, a_pygameHolder: PygameHolder):
            print(f"Update: {a_animation.curve.progress}")
            a_uiElement.internalRect.x = originalX + a_animation.curve.progress * 100
            a_uiManager.Recalculate(a_pygameHolder)
        def LeWonk(a_animation: Animation, a_pygameHolder: PygameHolder):
            a_uiElement.internalRect.x = originalX + 100 - a_animation.curve.progress * 100
            a_uiManager.Recalculate(a_pygameHolder)
        def LeDonk(a_animation: Animation, a_pygameHolder: PygameHolder):
            a_uiElement.internalRect.x = originalX
            a_uiManager.Recalculate(a_pygameHolder)
        def LeRonk(a_animation: Animation, a_pygameHolder: PygameHolder):
            print("Done")
            animationManager.animations[f"{a_uiElement.id}AnimBack"] =  Animation(LinearCurve(0, 0, 2), onUpdate=LeWonk, onEnd=LeDonk)
        animationManager.animations[f"{a_uiElement.id}AnimForward"] =  Animation(LinearCurve(0, 0, 2), onUpdate=LeTonk, onEnd=LeRonk)
        return True
    
    def LePonk(a_pygameHolder: PygameHolder, a_uiManager: UIManager, a_position: Vector2, a_uiElement: UIElement):
        screen = Screen.SETTINGS
        uiManager.layers[0].active = False
        return True

    uiManager.layers.append(UILayer(a_active=True, a_elements=["play"]))
    uiManager.elements["play"] = UIElement(
        "play", 
        a_parentAnchor=UIAnchor.TOP_CENTER, 
        a_internalRect=FRect(400, 100, 280, 50), 
        a_data={
            "text": "Play",
            "rect_color": Constants.BLUE
        },
        a_onDraw=[
            ("top", DrawFilledRect),
            ("text", DrawText)
        ], 
        a_postRecalculate=[
            ("text", RecalculateText)
        ],
        a_onLeftMouseDown=[
            ("play", LePonk)
        ]
    )

    uiManager.Recalculate(pygameHolder)

    game.SearchMods()
    for _, mod in game.modManager.mods.items():
        game.LoadModContent(mod)

    think: MapRenderer = MapRenderer(game, Map("base_game:test_map", "base_game:test_map/map_000", []))

    think.RenderFullMap(game)
    i = 0
    j = 0

    while pygameHolder.running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygameHolder.running = False
                case pygame.MOUSEBUTTONDOWN:
                    if uiManager.HandleInput(pygameHolder, Vector2(pygame.mouse.get_pos()), event.button):
                        ...

        if pygameHolder.deltaAccumulator <= 0:
            pygameHolder.deltaAccumulator = 1.0 / 60
            keys = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pressed()

            if keys[pygame.K_q]:
                print(f"Plus: {i}")
                i = (i + 1) % len(think.topViews)
            if keys[pygame.K_e]:
                print(f"Minus: {i}")
                i = (i + len(think.topViews) - 1) % len(think.topViews)
            if keys[pygame.K_w]:
                print(f"Plus: {i}")
                j = (j + 1) % 6
            if keys[pygame.K_s]:
                print(f"Minus: {i}")
                j = (j + 5) % 6

            ...
        else:
            pygameHolder.deltaAccumulator -= pygameHolder.deltaTime

        animationManager.Update(pygameHolder)
        uiManager.Update(pygameHolder)

        pygameHolder.screen.fill(Constants.LIGHT_GRAY)

        ...
        match screen:
            case Screen.MAIN_MENU:
                ...
            case Screen.SETTINGS:
                ...
        ...


        pygameHolder.screen.blit(uiManager.Render(pygameHolder))

        #print(think.renderedTileLayers[i])

        pygameHolder.screen.blit(pygame.transform.scale_by(think.renderedTileLayers[i], j + 1), (100, 100))
        pygameHolder.screen.blit(pygame.transform.scale_by(think.topViews[i], j + 1), (500, 100))
        pygame.display.flip()
        pygameHolder.Tick()
    
    pygameHolder.Exit()

if __name__ == "__main__":
    main()

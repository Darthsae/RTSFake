# fmt: off

import sys
import pygame
from pygame import Surface, Font, Clock
from typing import Final

class PygameHolder:
    FONT_SIZES: Final[list[int]] = [6, 7, 8, 10, 12, 14, 18, 20, 22, 24, 26, 30, 36, 48, 54, 60]

    def __init__(self, a_screenSize: tuple[int, int], a_fps: float) -> None:
        pygame.init()
        self.screen: Surface = pygame.display.set_mode(a_screenSize)
        self.fonts: dict[int, Font] = {fontSize: Font(None, fontSize) for fontSize in PygameHolder.FONT_SIZES}
        self.clock: Clock = Clock()
        self.running: bool = True
        self.deltaTime: float = 0
        self.deltaAccumulator: float = 0
        self.fps: float = a_fps
        self.inverseFPS: float = 1 / self.fps
    
    def Tick(self) -> None:
        self.deltaTime = min(self.clock.tick(self.fps) * 0.001, self.inverseFPS)
    
    def Exit(self) -> None:
        pygame.quit()
        sys.exit()


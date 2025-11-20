from __future__ import annotations

# fmt: off

from pygame import Color
from typing import Final

# Screen
SCREEN_WIDTH:  Final[int] = 1920
SCREEN_HEIGHT: Final[int] = 1080
SCREEN_SIZE: Final[tuple[int, int]] = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Tiles
TILE_SIZE: Final[int] = 16
METERS_PER_TILE: Final[int] = 1

# Colors
EMPTY:        Final[Color] = Color(  0,   0,   0,   0)
WHITE:        Final[Color] = Color(255, 255, 255, 255)
BLACK:        Final[Color] = Color(  0,   0,   0, 255)
LIGHT_GRAY:   Final[Color] = Color(220, 220, 220, 255)
GRAY:         Final[Color] = Color(200, 200, 200, 255)
DARK_GRAY:    Final[Color] = Color(145, 145, 145, 255)
BRIGHT_BLUE:  Final[Color] = Color(  0,   0, 255, 255)
LIGHT_BLUE:   Final[Color] = Color(175, 175, 255, 255)
BLUE:         Final[Color] = Color(100, 100, 255, 255)
DARK_BLUE:    Final[Color] = Color(  0,   0, 175, 255)
BRIGHT_GREEN: Final[Color] = Color(  0, 255,   0, 255)
LIGHT_GREEN:  Final[Color] = Color(175, 255, 175, 255)
GREEN:        Final[Color] = Color(100, 255, 100, 255)
DARK_GREEN:   Final[Color] = Color(  0, 255,   0, 255)
BRIGHT_RED:   Final[Color] = Color(255,   0,   0, 255)
LIGHT_RED:    Final[Color] = Color(255, 175, 175, 255)
RED:          Final[Color] = Color(255, 100, 100, 255)
DARK_RED:     Final[Color] = Color(175,   0,   0, 255)
from __future__ import annotations

# fmt: off

from itertools import islice
from math import floor
from pygame import Surface
import pygame

from ..game.world.unit.UnitInstance import UnitInstance

from ..game.data.map.LevelData import LevelData

from ..game.data.map.MapData import MapData
from ..game.world.Map import Map
from .. import Constants
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..assets.TextureAsset import TextureAsset
    from ..game.Game import Game

mapping: dict[tuple[bool, bool, bool, bool], tuple[int, int]] = {
    ( True, False, False, False): ( 0,  0),
    (False,  True, False, False): (16,  0),
    (False, False,  True, False): (32,  0),
    (False, False, False,  True): (48,  0),
    ( True,  True, False, False): ( 0, 16),
    (False,  True, False,  True): (16, 16),
    (False, False,  True,  True): (32, 16),
    ( True, False,  True, False): (48, 16),
    ( True,  True,  True, False): ( 0, 32),
    ( True, False,  True,  True): (16, 32),
    (False,  True,  True,  True): (32, 32),
    ( True,  True, False,  True): (48, 32),
    ( True,  True,  True,  True): ( 0, 48),
    ( True, False, False,  True): (16, 48),
    (False,  True,  True, False): (32, 48),
}

class MapRenderer:
    def __init__(self, a_game: Game, a_map: Map) -> None:
        self.map: Map = a_map
        levelData: LevelData|None = a_game.registries.Levels.Get(a_map.levelID)
        if levelData is None:
            raise RuntimeError(f"The level: {a_map.levelID}, does not exist.")
        self.mapData: MapData = levelData.maps[a_map.mapID]
        self.renderedTileLayers: list[Surface] = [Surface((self.mapData.width * Constants.TILE_SIZE, self.mapData.length * Constants.TILE_SIZE), pygame.SRCALPHA) for _ in range(self.mapData.height)]
        self.topViews: list[Surface] = [Surface((self.mapData.width * Constants.TILE_SIZE, self.mapData.length * Constants.TILE_SIZE), pygame.SRCALPHA) for _ in range(self.mapData.height)]

    def RenderFullMap(self, a_game: Game) -> None:
        [layer.fill(Constants.EMPTY) for layer in self.renderedTileLayers]
        tiles: list[TextureAsset] = [a_game.textureManager.textures[a_game.registries.Tiles[tileType].texture] for tileType in self.mapData.keys]
        x, y, z, topLeft, topRight, bottomLeft, bottomRight = 0, 0, 0, 0, 0, 0, 0
        useHeight, useWidth = self.mapData.length - 1, self.mapData.width - 1
        useIter = (self.mapData.length) * (self.mapData.width)
        useIterer = useHeight * useWidth
        for i in range(useIterer * self.mapData.height):
            x, y, z = i % useWidth, (i // useWidth) % useHeight, i // (useIterer)
            topLeft     = self.mapData.tiles[x + y * (self.mapData.width) + z * useIter]
            topRight    = self.mapData.tiles[(x + 1) + y * (self.mapData.width) + z * useIter]
            bottomLeft  = self.mapData.tiles[x + (y + 1) * (self.mapData.width) + z * useIter]
            bottomRight = self.mapData.tiles[(x + 1) + (y + 1) * (self.mapData.width) + z * useIter]
            print(f"{x} {y} {z} : {topLeft} {topRight} {bottomLeft} {bottomRight}")
            self.renderedTileLayers[z].blits([(tiles[tileType].textureSurface, (x * Constants.TILE_SIZE, y * Constants.TILE_SIZE), (mapping[(topLeft == tileType, topRight == tileType, bottomLeft == tileType, bottomRight == tileType)], (16, 16))) for tileType in {topLeft, topRight, bottomLeft, bottomRight} if tileType != -1])

        self.RenderTopViews(a_game)
    
    def RenderTopViews(self, a_game: Game) -> None:
        [layer.fill(Constants.EMPTY) for layer in self.topViews]
        [self.topViews[-z].blits([(layer, (0, 0)) for layer in islice(reversed(self.renderedTileLayers), z + 1)]) for z in range(self.mapData.height)]

    def RenderTheThing(self, a_game: Game, a_surface: Surface, a_level: int) -> None:
        layers: list[list[UnitInstance]] = [
            [] for _ in range(len(self.map.units))
        ]
        [layers[floor(unit.position.z)].append(unit) for unit in self.map.units]

        for i, ent in enumerate(reversed(layers)):
            for uni in ent:
                a_surface.fill((0, 200, 158), (uni.position.x * Constants.TILE_SIZE, uni.position.y * Constants.TILE_SIZE, Constants.TILE_SIZE * 0.2, Constants.TILE_SIZE * 0.2))
            a_surface.blit(self.renderedTileLayers[-i])
            if i >= a_level:
                break


    #def RenderMapAlt(self, a_game: Game) -> None:
    #    self.renderedTiles.fill(Constants.BLACK)
    #    tiles: list[TextureAsset] = [a_game.textureManager.textures[a_game.registries.Tiles.Get(a).texture] for a in self.mapData.keys]
    #    useHeight, useWidth = self.mapData.height - 1, self.mapData.width - 1
    #        
    #    self.renderedTiles.blits(
    #        [
    #            (tiles[tileType].textureSurface, 
    #                (
    #                    (i % useHeight) * Constants.TILE_SIZE, 
    #                    (i // useHeight) * Constants.TILE_SIZE
    #                ), 
    #                (
    #                    mapping[((self.mapData.tiles[(i % useWidth) + (i // useHeight) * useHeight]) == tileType, (self.mapData.tiles[((i % useWidth) + 1) + (i // useHeight) * useHeight]) == tileType, (self.mapData.tiles[(i % useWidth) + ((i // useHeight) + 1) * useHeight]) == tileType, (self.mapData.tiles[((i % useWidth) + 1) + ((i // useHeight) + 1) * useHeight]) == tileType)], 
    #                    (16, 16)
    #                )
    #            ) for i in range(
    #                useHeight * useWidth
    #            ) for tileType in {
    #                self.mapData.tiles[(i % useWidth) + (i // useHeight) * useHeight], 
    #                self.mapData.tiles[((i % useWidth) + 1) + (i // useHeight) * useHeight], 
    #                self.mapData.tiles[(i % useWidth) + ((i // useHeight) + 1) * useHeight], 
    #                self.mapData.tiles[((i % useWidth) + 1) + ((i // useHeight) + 1) * useHeight]
    #            } if tileType != -1
    #        ]
    #    )
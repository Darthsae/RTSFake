# fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from collections.abc import Iterable
    from .Vec3I import Vec3I

@dataclass(unsafe_hash=True)
class AABB3I:
    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0
    l: int = 0
    h: int = 0

    def __add__(self, other: Vec3I) -> AABB3I:
        return AABB3I(self.x + other.x, self.y + other.y, self.z + other.z, self.w, self.l, self.h)

    def __sub__(self, other: Vec3I) -> AABB3I:
        return AABB3I(self.x - other.x, self.y - other.y, self.z - other.z, self.w, self.l, self.h)

    def __mul__(self, other: int|float) -> AABB3I:
        return AABB3I(self.x, self.y, self.z, int(self.w * other), int(self.l * other), int(self.h * other))

    def __div__(self, other: int|float) -> AABB3I:
        return AABB3I(self.x, self.y, self.z, int(self.w / other), int(self.l / other), int(self.h / other))
    
    def __pow__(self, other: complex) -> AABB3I:
        return AABB3I(self.x, self.y, self.z, pow(self.w, other), pow(self.l, other), pow(self.h, other))
    
    @classmethod
    def FromList(cls, a_data: Iterable[int]) -> Self:
        return cls(*a_data)
    
    def ToList(self) -> list[int]:
        return [self.x, self.y, self.z, self.w, self.l, self. h]
from __future__ import annotations

# fmt: off
from dataclasses import dataclass
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from collections.abc import Iterable

@dataclass(unsafe_hash=True)
class Vec3F:
    x: float = 0
    y: float = 0
    z: float = 0

    def __add__(self, other: Vec3F) -> Vec3F:
        return Vec3F(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vec3F) -> Vec3F:
        return Vec3F(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: int|float) -> Vec3F:
        return Vec3F(self.x * other, self.y * other, self.z * other)

    def __div__(self, other: int|float) -> Vec3F:
        return Vec3F(self.x / other, self.y / other, self.z / other)
    
    def __pow__(self, other: complex) -> Vec3F:
        return Vec3F(pow(self.x, other), pow(self.y, other), pow(self.z, other))
    
    @classmethod
    def FromList(cls, a_data: Iterable[float]) -> Self:
        return cls(*a_data)
    
    def ToList(self) -> list[float]:
        return [self.x, self.y, self.z]
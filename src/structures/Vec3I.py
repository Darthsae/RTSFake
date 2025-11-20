from __future__ import annotations

# fmt: off
from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Vec3I:
    x: int = 0
    y: int = 0
    z: int = 0

    def __add__(self, other: Vec3I) -> Vec3I:
        return Vec3I(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vec3I) -> Vec3I:
        return Vec3I(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: int|float) -> Vec3I:
        return Vec3I(int(self.x * other), int(self.y * other), int(self.z * other))

    def __div__(self, other: int|float) -> Vec3I:
        return Vec3I(int(self.x / other), int(self.y / other), int(self.z / other))
    
    def __pow__(self, other: complex) -> Vec3I:
        return Vec3I(pow(self.x, other), pow(self.y, other), pow(self.z, other))
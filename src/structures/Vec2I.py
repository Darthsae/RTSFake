# fmt: off
from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Vec2I:
    x: int = 0
    y: int = 0

    def __add__(self, other: Vec2I) -> Vec2I:
        return Vec2I(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vec2I) -> Vec2I:
        return Vec2I(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int|float) -> Vec2I:
        return Vec2I(int(self.x * other), int(self.y * other))

    def __div__(self, other: int|float) -> Vec2I:
        return Vec2I(int(self.x / other), int(self.y / other))
    
    def __pow__(self, other: complex) -> Vec2I:
        return Vec2I(pow(self.x, other), pow(self.y, other))
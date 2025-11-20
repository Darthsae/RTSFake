from __future__ import annotations

#fmt: off

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Self, override

@dataclass
class Curve(ABC):
    progress: float

    @abstractmethod
    def Update(self, a_deltaTime: float) -> None:
        ...

@dataclass
class LinearCurve(Curve):
    distance: float
    length: float
    
    @override
    def Update(self, a_deltaTime: float) -> None:
        self.distance = min(self.distance + a_deltaTime, self.length)
        self.progress = self.distance / self.length
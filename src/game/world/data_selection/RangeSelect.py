# fmt: off

from dataclasses import dataclass
from operator import gt, ge, lt, le
from ....util.Typing import AnyDict, SupportsComparison
from typing import Literal, Self

@dataclass
class RangeSelect[T: SupportsComparison]:
    mode: Literal["include", "exclude"]
    min: T
    minInclusive: bool
    max: T
    maxInclusive: bool

    def Test(self, a_value: T) -> bool:
        return ((ge if self.minInclusive else gt)(self.min, a_value) and (le if self.maxInclusive else lt)(self.min, a_value)) == (True if self.mode == "include" else False)
    
    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            a_data["mode"],
            a_data["min"],
            a_data["minInclusive"],
            a_data["max"],
            a_data["maxInclusive"]
        )
    
    def ToDict(self) -> AnyDict:
        return {
            "mode": self.mode,
            "min": self.min,
            "min_inclusive": self.minInclusive,
            "max": self.max,
            "max_inclusive": self.maxInclusive
        }
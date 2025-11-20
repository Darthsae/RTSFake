from __future__ import annotations

#fmt: off

from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import StrEnum, auto
from typing import TYPE_CHECKING, Self, Final, ClassVar
if TYPE_CHECKING:
    from ....util.Typing import AnyDict
    from ...Game import Game

class BooleanUnaryOperatorType(StrEnum):
    NOT = auto()

class BooleanBinaryOperatorType(StrEnum):
    AND  = auto()
    NAND = auto()
    OR   = auto()
    NOR  = auto()
    XOR  = auto()

class ComparisonBinaryOperatorType(StrEnum):
    GT  = auto()
    GTE = auto()
    LT  = auto()
    LTE = auto()


@dataclass
class ComplexCodeNode[R](ABC):
    id: str

    @abstractmethod
    def Evaluate(self, a_game: Game, a_data: AnyDict) -> R:
        ...

    @abstractmethod
    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        ...
    
    @abstractmethod
    def ToDict(self) -> AnyDict:
        ...

@dataclass
class BooleanBinaryOperatorCodeNode(ComplexCodeNode[bool]):
    ID: ClassVar[Final[str]] = "boolean_binary_operator"
    operator: BooleanBinaryOperatorType
    left: ComplexCodeNode[bool]
    right: ComplexCodeNode[bool]


@dataclass
class ComparisonBinaryOperatorCodeNode(ComplexCodeNode[bool]):
    ID: ClassVar[Final[str]] = "comparison_binary_operator"
    operator: ComparisonBinaryOperatorType
    left: ComplexCodeNode[int|float]
    right: ComplexCodeNode[int|float]
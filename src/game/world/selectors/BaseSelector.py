from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ....util.Typing import AnyDict
    from ...Game import GameRegistries

@dataclass
class BaseSelector[T](ABC):
    @abstractmethod
    def Select(self, a_selectable: list[T], a_registries: GameRegistries, a_data: AnyDict) -> list[T]: ...


from __future__ import annotations

# fmt: off

from re import Pattern
import re

from .BaseSelector import BaseSelector
from typing import Self, Any, override, TYPE_CHECKING
if TYPE_CHECKING:
    from ..unit.UnitInstance import UnitInstance
    from ....util.Typing import AnyDict
    from ...data.GameRegistries import GameRegistries
    from ..predicates.UnitStatInstancePredicate import UnitStatInstancePredicate
    from ..predicates.UnitAttributeInstancePredicate import UnitAttributeInstancePredicate
    from ..predicates.UnitResourceInstancePredicate import UnitResourceInstancePredicate

class UnitInstanceSelector(BaseSelector[UnitInstance]):
    def __init__(self, /, a_owner: str = ".*", a_faction: str = ".*", a_stats: UnitStatInstancePredicate|None = None, a_resources: UnitResourceInstancePredicate|None = None, a_attributes: UnitAttributeInstancePredicate|None = None, a_limit: int = -1):
        self.owner: Pattern[str] = re.compile(a_owner)
        self.faction: Pattern[str] = re.compile(a_faction)
        self.stats: UnitStatInstancePredicate = UnitStatInstancePredicate([]) if a_stats is None else a_stats
        self.resources: UnitResourceInstancePredicate = UnitResourceInstancePredicate([]) if a_resources is None else a_resources
        self.attributes: UnitAttributeInstancePredicate = UnitAttributeInstancePredicate([]) if a_attributes is None else a_attributes
        self.limit: int = a_limit

    @override
    def Select(self, a_selectable: list[UnitInstance], a_registries: GameRegistries, a_data: dict[str, Any]) -> list[UnitInstance]:
        counter: int = -1
        def I_Selectable(a_element: UnitInstance) -> bool:
            nonlocal counter
            if self.owner.search(a_element.owner) is None:
                return False
            if self.faction.search(a_element.faction) is None:
                return False
            counter += 1 if self.limit > 0 else 0
            return counter <= self.limit
        return list(filter(I_Selectable, a_selectable))

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls()
    
    def ToDict(self) -> AnyDict:
        return {
            "owner": self.owner.pattern,
            "faction": self.faction.pattern,
            "stats": self.stats.ToDict(),
            "resources": self.resources.ToDict(),
            "attributes": self.attributes.ToDict(),
            "limit": self.limit
        }

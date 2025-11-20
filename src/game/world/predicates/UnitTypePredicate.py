from __future__ import annotations

# fmt: off
from re import Pattern
import re

from ...data.unit.UnitType import UnitType
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ....util.Typing import AnyDict
    from ..predicates.TagsPredicate import TagsPredicate
    from ..predicates.UnitStatSpecPredicate import UnitStatSpecPredicate
    from ..predicates.UnitAttributeSpecPredicate import UnitAttributeSpecPredicate
    from ..predicates.UnitResourceSpecPredicate import UnitResourceSpecPredicate

class UnitTypePredicate:
    def __init__(self, /, a_name: str = ".*", a_description: str = ".*", a_faction: str = ".*", a_tags: TagsPredicate|None = None, a_stats: UnitStatSpecPredicate|None = None, a_resources: UnitResourceSpecPredicate|None = None, a_attributes: UnitAttributeSpecPredicate|None = None) -> None:
        self.name: Pattern[str] = re.compile(a_name)
        self.description: Pattern[str] = re.compile(a_description)
        self.faction: Pattern[str] = re.compile(a_faction)
        self.tags: TagsPredicate = TagsPredicate([]) if a_tags is None else a_tags
        self.stats: UnitStatSpecPredicate = UnitStatSpecPredicate([]) if a_stats is None else a_stats
        self.resources: UnitResourceSpecPredicate = UnitResourceSpecPredicate([]) if a_resources is None else a_resources
        self.attributes: UnitAttributeSpecPredicate = UnitAttributeSpecPredicate([]) if a_attributes is None else a_attributes

    def Validate(self, a_unitType: UnitType) -> bool:
        return self.name.search(a_unitType.name) is not None                \
            and self.description.search(a_unitType.description) is not None \
            and self.faction.search(a_unitType.faction) is not None         \
            and self.tags.Validate(a_unitType.tags)                         \
            and self.stats.Validate(a_unitType.statSpecs)                   \
            and self.resources.Validate(a_unitType.resourceSpecs)           \
            and self.attributes.Validate(a_unitType.attributeSpecs)

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            a_data["name"],
            a_data["description"],
            a_data["faction"],
            TagsPredicate.FromDict(a_data["tags"]),
            UnitStatSpecPredicate.FromDict(a_data["stats"]),
            UnitResourceSpecPredicate.FromDict(a_data["resources"]),
            UnitAttributeSpecPredicate.FromDict(a_data["attributes"])
        )

    def ToDict(self) -> AnyDict:
        return {
            "name": self.name.pattern,
            "description": self.description.pattern,
            "faction": self.faction.pattern,
            "tags": self.tags.ToDict(),
            "stats": self.stats.ToDict(),
            "resources": self.resources.ToDict(),
            "attributes": self.attributes.ToDict()
        }

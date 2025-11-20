from __future__ import annotations

# fmt: off

from dataclasses import dataclass

from ....util.Typing import AnyDict
from .UnitStatSpec import UnitStatSpec
from .UnitResourceSpec import UnitResourceSpec
from .UnitAttributeSpec import UnitAttributeSpec

from typing import Self, Any, cast, TYPE_CHECKING

@dataclass
class UnitType:
    id: str
    name: str
    description: str
    faction: str
    tags: list[str]
    statSpecs: dict[str, UnitStatSpec]
    resourceSpecs: dict[str, UnitResourceSpec]
    attributeSpecs: dict[str, UnitAttributeSpec]

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        unitType: UnitType = cls(
            a_data["id"],
            a_data["name"],
            a_data["description"],
            a_data["faction"],
            a_data["tags"],
            {key: UnitStatSpec.FromDict(value) for key, value in cast(dict[str, Any], a_data["stats"]).items()},
            {key: UnitResourceSpec.FromDict(value) for key, value in cast(dict[str, Any], a_data["resources"]).items()},
            {key: UnitAttributeSpec.FromDict(value) for key, value in cast(dict[str, Any], a_data["attributes"]).items()}
        )

        return unitType

    def ToDict(self) -> AnyDict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "faction": self.faction,
            "tags": self.tags,
            "stats": {key: spec.ToDict() for key, spec in self.statSpecs.items()},
            "resources": {key: spec.ToDict() for key, spec in self.resourceSpecs.items()},
            "attributes": {key: spec.ToDict() for key, spec in self.attributeSpecs.items()}
        }

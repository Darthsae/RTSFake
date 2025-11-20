from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Self
if TYPE_CHECKING:
    from .UnitStatSpec import UnitStatSpec
    from .UnitResourceSpec import UnitResourceSpec
    from .UnitAttributeSpec import UnitAttributeSpec
    from ....structures.Vec3F import Vec3F
    from ....util.Typing import AnyDict

@dataclass
class UnitSpawnData:
    unitID: str
    unitPosition: Vec3F
    unitMap: str
    unitOwner: str
    factionOverride: str|None
    nameOverride: str|None
    descriptionOverride: str|None
    tagsOverride: list[str]
    statSpecsOverride: dict[str, UnitStatSpec]
    resourceSpecsOverride: dict[str, UnitResourceSpec]
    attributeSpecsOverride: dict[str, UnitAttributeSpec]

    @classmethod
    def FromDict(cls, a_data: dict[str, Any]) -> Self:
        return cls(
            a_data["unit_id"],
            Vec3F.FromList(a_data["unit_pos"]),
            a_data["unit_map"],
            a_data["unit_owner"],
            a_data.get("faction", None),
            a_data.get("name", None),
            a_data.get("description", None),
            a_data["tags"],
            a_data["stats"],
            a_data["resources"],
            a_data["attributes"]
        )

    def ToDict(self) -> AnyDict:
        toReturn: AnyDict = {
            "unit_id": self.unitID,
            "unit_pos": self.unitPosition.ToList(),
            "unit_map": self.unitMap,
            "unit_owner": self.unitOwner,
            "tags": self.tagsOverride,
            "stats": {statSpecOverrideName: statSpecOverride.ToDict() for statSpecOverrideName, statSpecOverride in self.statSpecsOverride.items()}
        }
        if self.factionOverride is not None:
            toReturn["faction"] = self.factionOverride
        if self.nameOverride is not None:
            toReturn["name"] = self.nameOverride
        if self.descriptionOverride is not None:
            toReturn["description"] = self.descriptionOverride
        return toReturn

from __future__ import annotations

# fmt: off

from typing import TYPE_CHECKING, Self

from ....structures.Vec3F import Vec3F

from .UnitStatInstance import UnitStatInstance
from .UnitResourceInstance import UnitResourceInstance
from .UnitAttributeInstance import UnitAttributeInstance
if TYPE_CHECKING:
    from ...data.unit.UnitType import UnitType
    from ...data.unit.UnitSpawnData import UnitSpawnData
    from ...data.GameRegistries import GameRegistries
    from ....util.Typing import AnyDict

class UnitInstance:
    def __init__(self, a_unitID: str, a_name: str, a_description: str, a_owner: str, a_faction: str, a_tags: list[str], a_stats: dict[str, UnitStatInstance], a_resources: dict[str, UnitResourceInstance], a_attributes: dict[str, UnitAttributeInstance], a_pos: Vec3F, a_map: str) -> None:
        self.unitID: str = a_unitID
        self.name: str = a_name
        self.description: str = a_description
        self.owner: str = a_owner
        self.faction: str = a_faction
        self.tags: list[str] = a_tags
        self.stats: dict[str, UnitStatInstance] = a_stats
        self.resources: dict[str, UnitResourceInstance] = a_resources
        self.attributes: dict[str, UnitAttributeInstance] = a_attributes
        self.position: Vec3F = a_pos
        self.map: str = a_map

    @classmethod
    def FromSpawnData(cls, a_gameRegistries: GameRegistries, a_unitSpawnData: UnitSpawnData) -> Self:
        unit: UnitType = a_gameRegistries.Units[a_unitSpawnData.unitID]
        return cls(
            a_unitSpawnData.unitID,
            unit.name if a_unitSpawnData.nameOverride is None else a_unitSpawnData.nameOverride,
            unit.description if a_unitSpawnData.descriptionOverride is None else a_unitSpawnData.descriptionOverride,
            a_unitSpawnData.unitOwner,
            unit.faction if a_unitSpawnData.factionOverride is None else a_unitSpawnData.factionOverride,
            [*unit.tags, *a_unitSpawnData.tagsOverride],
            {statID: UnitStatInstance.FromSpec(statSpec) for statID, statSpec in (unit.statSpecs | a_unitSpawnData.statSpecsOverride).items()},
            {resourceID: UnitResourceInstance.FromSpec(resourceSpec) for resourceID, resourceSpec in (unit.resourceSpecs | a_unitSpawnData.resourceSpecsOverride).items()},
            {attributeID: UnitAttributeInstance.FromSpec(attributeSpec) for attributeID, attributeSpec in (unit.attributeSpecs | a_unitSpawnData.attributeSpecsOverride).items()},
            a_unitSpawnData.unitPosition,
            a_unitSpawnData.unitMap
        )

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            a_data["id"], a_data["name"], a_data["description"], a_data["owner"], a_data["faction"], a_data["tags"],
            {statID: UnitStatInstance.FromDict(statSpec) for statID, statSpec in a_data["stats"]},
            {resourceID: UnitResourceInstance.FromDict(resourceSpec) for resourceID, resourceSpec in a_data["resources"]},
            {attributeID: UnitAttributeInstance.FromDict(attributeSpec) for attributeID, attributeSpec in a_data["attributes"]},
            Vec3F.FromList(a_data["position"]), a_data["map"]
        )

    def ToDict(self) -> AnyDict:
        return {
            "id": self.unitID,
            "name": self.name,
            "description": self.description,
            "owner": self.owner,
            "faction": self.faction,
            "tags": self.tags,
            "stats": {statID: stat.ToDict() for statID, stat in self.stats.items()},
            "resources": {resourceID: resource.ToDict() for resourceID, resource in self.resources.items()},
            "attributes": {attributeID: attribute.ToDict() for attributeID, attribute in self.attributes.items()},
            "position": self.position.ToList(),
            "map": self.map
        }


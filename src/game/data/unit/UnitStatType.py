from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ....util.Typing import AnyDict

@dataclass
class UnitStatType:
    id: str
    name: str
    description: str
    icon: str

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(a_data["stat_id"], a_data["stat_name"], a_data.get("stat_description", ""), a_data.get("stat_icon", "no_texture"))

    def ToDict(self) -> AnyDict:
        return {
            "stat_id": self.id,
            "stat_name": self.name,
            "stat_description": self.description,
            "stat_icon": self.icon
        }
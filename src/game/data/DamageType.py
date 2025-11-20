from __future__ import annotations

#fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Self
if TYPE_CHECKING:
    from ...util.Typing import AnyDict

@dataclass
class DamageType:
    id: str
    name: str
    description: str
    icon: str

    @classmethod
    def FromDict(cls, a_data: dict[str, Any]) -> Self:
        return cls(
            a_data["id"],
            a_data["name"],
            a_data["description"],
            a_data["icon"]
        )
    
    def ToDict(self) -> AnyDict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "icon": self.icon
        }
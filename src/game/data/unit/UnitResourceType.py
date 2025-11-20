from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Self
if TYPE_CHECKING:
    ...

@dataclass
class UnitResourceType:
    id: str
    name: str
    description: str
    icon: str

    @classmethod
    def FromDict(cls, a_data: dict[str, Any]) -> Self:
        return cls(a_data["resource_id"], a_data["resource_name"], a_data.get("resource_description", ""), a_data.get("resource_icon", "no_texture"))

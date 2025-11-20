from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ...util.Typing import AnyDict

@dataclass
class Mod:
    id: str
    name: str
    description: str
    version: int

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        print(a_data)
        return cls(a_data["id"], a_data["name"], a_data.get("description", ""), a_data["version"])
    
    def ToDict(self) -> AnyDict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "version": self.version
        }


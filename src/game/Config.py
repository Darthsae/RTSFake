from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ..util.Typing import AnyDict

@dataclass
class Config:
    id: str

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            a_data["id"]
        )

    def ToDict(self) -> AnyDict:
        return {
            "id": self.id
        }

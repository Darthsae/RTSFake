from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from enum import StrEnum, auto
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ....util.Typing import AnyDict

class Presence(StrEnum):
    REQUIRED  = auto()
    OPTIONAL  = auto()
    FORBIDDEN = auto()

@dataclass
class TagIndividualData:
    tag: str
    presence: Presence

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            a_data["tag"],
            Presence(a_data["presence"]),
        )

    def ToDict(self) -> AnyDict:
        return {
            "tag": self.tag,
            "presence": str(self.presence)
        }

class TagsPredicate:
    def __init__(self, a_tags: list[TagIndividualData]) -> None:
        self.tags: list[TagIndividualData] = a_tags

    def Validate(self, a_tags: list[str]) -> bool:
        for tag in self.tags:
            present: bool = tag.tag in a_tags
            match tag.presence:
                case Presence.REQUIRED:
                    if not present:
                        return False
                case Presence.OPTIONAL:
                    ...
                case Presence.FORBIDDEN:
                    if present:
                        return False
        return True

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            [TagIndividualData.FromDict(data) for data in a_data["tags"]]
        )

    def ToDict(self) -> AnyDict:
        return {
            "tags": [tag.ToDict() for tag in self.tags]
        }

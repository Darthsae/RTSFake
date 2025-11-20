from __future__ import annotations

# fmt: off

from dataclasses import dataclass
from ..selectors.UnitSelector import UnitInstanceSelector
from .BaseEffect import BaseEffect
from typing import TYPE_CHECKING, Self
if TYPE_CHECKING:
    from ....util.Typing import AnyDict

@dataclass
class DespawnUnitEffect(BaseEffect):
    unit: UnitInstanceSelector

    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        return cls(
            "despawn_unit_effect",
            UnitInstanceSelector.FromDict(a_data["unit"])
        )


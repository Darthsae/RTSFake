from __future__ import annotations

#fmt: off

from typing import Any, Annotated
from annotated_types import Ge

type AnyDict = dict[str, Any]
type JSONLiteral = str|int|float|bool|None
type JSONCollections[T] = list[T]|dict[str, T]
type JSONSerializable = dict[str, JSONLiteral|JSONCollections[JSONLiteral]]
type UInt = Annotated[int, Ge(0)]
type Version = tuple[UInt, UInt, UInt, UInt]
from __future__ import annotations

# fmt: off

from dataclasses import dataclass
import dataclasses

from typing import TYPE_CHECKING, overload
if TYPE_CHECKING:
    from collections.abc import Iterator

@dataclass
class Registry[T]:
    entries: dict[str, T] = dataclasses.field(default_factory=dict[str, T]) 

    def __len__(self) -> int:
        return len(self.entries)

    def __getitem__(self, key: str) -> T:
        if key in self.entries:
            return self.entries[key]
        raise KeyError(key)
    
    def __contains__(self, key: str) -> bool:
        return key in self.entries
    
    def Register(self, a_id: str, a_registerable: T) -> None:
        self.entries[a_id] = a_registerable

    @overload
    def Get(self, key: str, default: T) -> T: ...
    @overload
    def Get(self, key: str, default: None = None) -> T|None: ...
    def Get(self, key: str, default: T|None = None) -> T|None:
        if key in self:
            return self[key]
        return default


    def Clear(self) -> None:
        self.entries.clear()

    def EntriesKeysIterator(self) -> Iterator[str]:
        return iter(self.entries.keys())
    
    def EntriesValuesIterator(self) -> Iterator[T]:
        return iter(self.entries.values())
    
    def EntriesItemsIterator(self) -> Iterator[tuple[str, T]]:
        return iter(self.entries.items())
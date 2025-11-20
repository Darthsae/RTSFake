# fmt: off

#from dataclasses import dataclass

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from os import DirEntry
    from collections.abc import Callable
    from ..util.Typing import AnyDict

class LocalizationLanguage:
    def __init__(self, a_id: str) -> None:
        self.id: str = a_id
        self.entries: dict[str, str] = {}

    def LoadEntriesFromDict(self, a_data: dict[str, str]) -> None:
        self.entries.update(a_data)

class LocalizationEntry:
    def __init__(self, a_id: str, a_value: str, /, a_onZero: Callable[[], None]|None = None):
        self.id: str = a_id
        self.value: str = a_value
        self.holders: int = 0
        self.OnZero: Callable[[], None]|None = a_onZero

    def Obtain(self) -> None:
        self.holders += 1

    def Release(self) -> None:
        self.holders -= 1
        if self.holders == 0 and self.OnZero is not None:
            self.OnZero()

#@dataclass
#class EntryCacheOperation:
#    entryID: str
#    acquisitions: int
#    timeOfLatestAcquisition: int

class LocalizationManager:
    #ENTRY_CACHE_MAX_RECENT_OPERATIONS: Final[int] = 100
    def __init__(self) -> None:
        self.languageID: str = "en_us"
        self.language: LocalizationLanguage = LocalizationLanguage("en_us")
        self.languages: dict[str, LocalizationLanguage] = {}
        self.entryCache: dict[str, LocalizationEntry] = {}
        #self.entryCacheRecentOperations: list[EntryCacheOperation] = []

    def Query(self, a_entryID: str) -> LocalizationEntry:
        self.entryCache[a_entryID] = (entry := self.entryCache.get(a_entryID, LocalizationEntry(a_entryID, self.language.entries.get(a_entryID, a_entryID))))
        entry.Obtain()
        return entry

    def Return(self, a_entryID: str) -> None:
        self.entryCache[a_entryID].Release()

    def ChangeLanguage(self, a_newLanguage: str) -> None:
        self.languageID = a_newLanguage
        self.Reload()

    def Reload(self):
        self.language = self.languages[self.languageID]
        for key, value in self.entryCache.items():
            value.value = self.language.entries.get(key, key)

    def m_CleanUpLocalizationEntryFactory(self, a_id: str) -> Callable[[], None]:
        def CleanUpLocalizationEntryFunction() -> None:
            self.entryCache.pop(a_id)
            #self.entryCacheRecentOperations.index(next(filter(lambda entry: entry.entryID == a_id, self.entryCacheRecentOperations)))
        return CleanUpLocalizationEntryFunction
    
    def LoadLanguageData(self, a_path: DirEntry[str]) -> int:
        with open(a_path) as localizationDataFile:
            data: AnyDict = json.load(localizationDataFile)
            language: str = a_path.name.removesuffix(".json")
            if language not in self.languages:
                self.languages[language] = LocalizationLanguage(language)
            self.languages[language].LoadEntriesFromDict(data)
        
        return 0

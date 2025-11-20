from __future__ import annotations

from .Config import Config

# fmt: off

class ConfigManager:
    def __init__(self) -> None:
        self.configs: dict[str, Config] = {}

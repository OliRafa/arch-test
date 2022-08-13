from pathlib import Path

from arch_test.core.module import Module


class Package:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.subpackages: list[Package] = []
        self.modules: list[Module] = []

    @property
    def name(self) -> str:
        return self.path.name.replace(".py", "")

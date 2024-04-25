from __future__ import annotations

from pathlib import Path

from arch_test.core.module import Module
from arch_test.core.package_iterator import PackageIterator


class Package(PackageIterator):
    def __init__(self, path: Path) -> None:
        self.path = path
        self.subpackages: list[Package] = []
        self.modules: list[Module] = []

    @property
    def name(self) -> str:
        return self.path.name.replace(".py", "")

    def get_package(self, name) -> Package:
        return super().get_package(name, self.subpackages)

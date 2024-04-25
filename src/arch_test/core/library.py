from __future__ import annotations

from arch_test.core.module import Module
from arch_test.core.package import Package
from arch_test.core.package_iterator import PackageIterator


class Library(PackageIterator):
    def __init__(
        self, packages: list[Package] = [], modules: list[Module] = []
    ) -> None:
        super().__init__()
        self.packages: list[Package] = packages
        self.modules: list[Module] = modules

    def get_package(self, name) -> Package:
        return super().get_package(name, self.packages)

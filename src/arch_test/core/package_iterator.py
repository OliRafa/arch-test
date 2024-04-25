from __future__ import annotations

from arch_test.core.exceptions import PackageNotFoundError


class PackageIterator:
    def __init__(self) -> None:
        pass

    def get_package(self, name, packages: list["Package"]) -> "Package":
        for package in packages:
            if package.name == name:
                return package

        for package in packages:
            try:
                return self.get_package(name, package.subpackages)

            except PackageNotFoundError:
                continue

        raise PackageNotFoundError(name)

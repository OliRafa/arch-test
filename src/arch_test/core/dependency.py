from __future__ import annotations

from pathlib import Path

from arch_test.core.exceptions import ModuleNotFoundError


class Dependency:
    def __init__(self, path: Path, parent: "Module") -> None:
        self.parent = parent
        self.path = path
        self.name = self.path.name
        self._upper_package_path = self.path.parents[1]

    def resolve(self):
        package_parent = self._traverse_vertically(self.parent)
        try:
            return next(filter(lambda x: x.name == self.name, package_parent.modules))
        except StopIteration:
            raise ModuleNotFoundError(self.path)

    def _traverse_vertically(self, object: "Module" | "Package") -> "Module":
        common_package_parent = self.parent
        while common_package_parent not in self._upper_package_path.parts:
            common_package_parent = common_package_parent.parent

        return common_package_parent

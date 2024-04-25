from __future__ import annotations

from pathlib import Path
from typing import Optional

from arch_test.core.parsers.dependency import (
    filter_python_builtin_modules,
    filter_third_party_dependencies,
    get_module_dependencies,
)


class Module:
    def __init__(self, path: Path, parent: "Library" | "Package") -> None:
        self.parent = parent
        self.path = path

    @property
    def name(self) -> str:
        return self.path.name.replace(".py", "")

    def get_dependencies(self) -> list[Optional[str]]:
        dependencies = get_module_dependencies(self.path)
        filtered_dependencies = filter_python_builtin_modules(dependencies)
        filtered_dependencies = filter_third_party_dependencies(filtered_dependencies)
        return filtered_dependencies

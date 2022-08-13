from __future__ import annotations

from pathlib import Path

from arch_test.core.library import Library
from arch_test.core.module import Module
from arch_test.core.package import Package


class PythonDependencyParser:
    def __init__(self) -> None:
        pass

    def parse(self, library_path: Path) -> Library:
        root_packages = self._parse_packages(library_path)
        root_modules = self._parse_modules(library_path)
        library = Library()
        library.packages = root_packages
        library.modules = root_modules
        return library

    def _parse_packages(self, library_path: Path) -> list[Package]:
        paths = library_path.glob("*")
        package_paths = filter(lambda x: x.is_dir(), paths)
        packages = list(map(lambda x: Package(x), package_paths))

        empty_packages = []
        for package in packages:
            package.subpackages = self._parse_packages(package.path)
            package.modules = self._parse_modules(package.path)

            if not package.subpackages and not package.modules:
                empty_packages.append(package)

        for empty_package in empty_packages:
            packages.remove(empty_package)

        return packages

    def _parse_modules(self, package_path: Path) -> list[Module]:
        paths = package_path.glob("*")
        module_paths = filter(
            lambda path: path.is_file() and path.name.endswith(".py"), paths
        )
        return list(map(lambda x: Module(x), module_paths))

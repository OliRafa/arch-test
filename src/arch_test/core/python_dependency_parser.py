from __future__ import annotations

from pathlib import Path

from arch_test.core.library import Library
from arch_test.core.module import Module
from arch_test.core.package import Package


class PythonDependencyParser:
    def __init__(self) -> None:
        pass

    def parse(self, library_path: Path) -> Library:
        library = Library()
        root_packages = self._parse_packages(library_path, library)
        root_modules = self._parse_modules(library_path, library)
        library.packages = root_packages
        library.modules = root_modules
        return library

    def _parse_packages(
        self, library_path: Path, parent: Library | Package
    ) -> list[Package]:
        paths = library_path.glob("*")
        package_paths = filter(lambda x: x.is_dir(), paths)
        packages = list(map(lambda x: Package(x, parent=parent), package_paths))

        empty_packages = []
        for package in packages:
            package.subpackages = self._parse_packages(package.path, package)
            package.modules = self._parse_modules(package.path, package)

            if not package.subpackages and not package.modules:
                empty_packages.append(package)

        for empty_package in empty_packages:
            packages.remove(empty_package)

        return packages

    def _parse_modules(
        self, package_path: Path, parent: Library | Package
    ) -> list[Module]:
        paths = package_path.glob("*")
        module_paths = filter(
            lambda path: path.is_file() and path.name.endswith(".py"), paths
        )
        return list(map(lambda x: Module(x, parent=parent), module_paths))

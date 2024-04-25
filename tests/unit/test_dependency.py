from pathlib import Path
from unittest.mock import MagicMock, Mock

from pytest import raises

from arch_test.core.dependency import Dependency
from arch_test.core.exceptions import ModuleNotFoundError
from arch_test.core.module import Module
from arch_test.core.package import Package


def test_given_dependency_path_should_resolve_the_name():
    path = Path("library/package÷subpackage/module")
    dependency = Dependency(path, Mock())

    assert dependency.name == "module"


def test_when_resolving_dependency_given_wrong_path_should_raise_exception():
    path = Path("library/wrong/path/to/module")
    module = Mock(name="something")
    package = MagicMock(modules=[module])
    module.parent = package

    with raises(ModuleNotFoundError):
        Dependency(path, module).resolve()


def test_when_dependent_module_is_in_the_same_package_should_return_module():
    package = Package(Path("library/package"), Mock())
    dependent_module = Module(Path("library/package/dependent_module"), package)
    base_module = Module(Path("library/package/base_module"), package)

    package.modules = [base_module, dependent_module]

    dependency = Dependency(Path("library/package/dependent_module"), base_module)
    resolved_module = dependency.resolve()

    assert resolved_module == dependent_module


def test_when_dependent_module_is_in_above_package_should_return_module():
    above_package = Package(Path("library/above_package"), Mock())
    dependent_module = Module(
        Path("library/another_package/dependent_module"), above_package
    )
    above_package.modules = [dependent_module]
    package = Package(Path("library/package"), above_package)
    base_module = Module(Path("library/package/base_module"), package)

    package.modules = [base_module]
    above_package.subpackages = [package]

    dependency = Dependency(
        Path("library/another_package/dependent_module"), base_module
    )
    resolved_module = dependency.resolve()

    assert resolved_module == dependent_module

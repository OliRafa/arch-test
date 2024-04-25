from pathlib import Path

from arch_test.core.library import Library, Package
from arch_test.core.module import Module
from arch_test.core.python_dependency_parser import PythonDependencyParser


def test_given_project_path_should_return_library_object(correct_project: Path):
    parser = PythonDependencyParser()
    library = parser.parse(correct_project)
    assert isinstance(library, Library)


def test_parser_should_return_library_with_packages(correct_project: Path):
    parser = PythonDependencyParser()
    library = parser.parse(correct_project)

    assert library.packages
    assert len(library.packages) == 2
    assert all(isinstance(package, Package) for package in library.packages)


def test_parse_packages_should_return_directories_only(correct_project: Path):
    parser = PythonDependencyParser()
    library = parser.parse(correct_project)
    assert all(package.path.is_dir() for package in library.packages)


def test_when_parsed_packages_have_subpackages_should_return_them(
    correct_project: Path,
):
    parser = PythonDependencyParser()
    library = parser.parse(correct_project)

    core_package = list(
        filter(lambda package: package.name == "core", library.packages)
    )[0]
    assert core_package.subpackages
    assert len(core_package.subpackages) == 2

    infra_package = list(
        filter(lambda package: package.name == "infra", library.packages)
    )[0]
    assert not infra_package.subpackages


def test_when_parsed_library_have_modules_should_return_them(correct_project: Path):
    parser = PythonDependencyParser()
    library = parser.parse(correct_project)

    assert library.modules
    assert library.modules[0].name == "__init__"


def test_when_parsed_packages_have_modules_should_return_them(correct_project: Path):
    parser = PythonDependencyParser()
    library = parser.parse(correct_project)

    infra_package = list(
        filter(lambda package: package.name == "infra", library.packages)
    )[0]

    assert infra_package.modules
    assert isinstance(infra_package.modules[0], Module)
    assert infra_package.modules[0].name == "rest_framework"


def test_parsed_modules_should_have_its_imported_dependencies(correct_project: Path):
    parser = PythonDependencyParser()
    library = parser.parse(correct_project)

    core_package = list(
        filter(lambda package: package.name == "core", library.packages)
    )[0]
    use_cases_package = list(
        filter(lambda package: package.name == "use_cases", core_package.subpackages)
    )[0]
    simple_use_case_module = use_cases_package.modules[0]

    dependencies = simple_use_case_module.get_dependencies()

    assert len(dependencies) > 0


# def test_parser_shouldnt_parse_non_programming_language_files_as_modules(
# correct_project: Path,
# ):
# parser = PythonDependencyParser()
# library = parser.parse(correct_project)
#
# infra_package = list(
# filter(lambda package: package.name == "infra", library.packages)
# )[0]
#
# assert infra_package.modules
# assert isinstance(infra_package.modules[0], Module)
# assert infra_package.modules[0].name == "rest_framework"


def test_library_shouldnt_have_packages_without_modules_or_subpackages(
    correct_project: Path,
):
    parser = PythonDependencyParser()
    library = parser.parse(correct_project)

    docs_package = list(
        filter(lambda package: package.name == "docs", library.packages)
    )

    assert not docs_package


def test_objects_should_have_its_parent_reference(correct_project: Path):
    parser = PythonDependencyParser()
    library = parser.parse(correct_project)

    a_module = library.modules[0]

    assert a_module.parent == library

    a_package = library.modules[0]

    assert a_package.parent == library

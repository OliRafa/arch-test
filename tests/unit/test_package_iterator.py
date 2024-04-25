# from unittest.mock import MagicMock, patch

from pytest import raises

from arch_test.core.exceptions import PackageNotFoundError
from arch_test.core.library import Library
from arch_test.core.package_iterator import PackageIterator


def test_given_core_package_name_should_return_root_package(
    correct_project_library: Library,
):
    package_iterator = PackageIterator()

    returned_package = package_iterator.get_package(
        "core", correct_project_library.packages
    )
    assert returned_package.name == "core"


def test_when_package_isnt_found_then_should_raise_exception(
    correct_project_library: Library,
):
    package_iterator = PackageIterator()

    with raises(PackageNotFoundError):
        package_iterator.get_package("not_a_package", correct_project_library.packages)


def test_given_subpackage_name_should_return_a_subpackage(
    correct_project_library: Library,
):
    package_iterator = PackageIterator()

    returned_package = package_iterator.get_package(
        "use_cases", correct_project_library.packages
    )
    assert returned_package.name == "use_cases"


# def test_get_package_recursive_should_ignore_packages_without_subpackages(
#     correct_project_library: Library,
# ):
#     package_iterator = PackageIterator()

#     with patch.object(
#         PackageIterator, "get_package", wraps=package_iterator.get_package
#     ) as mock:
#         package_iterator.get_package("use_cases", correct_project_library.packages)
#         for call in mock.call_args_list:
#             print(call)

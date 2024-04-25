from pathlib import Path

from arch_test.core.module import Module


def test_modules_should_have_name_property(correct_project: Path):
    module = Module(correct_project)

    assert module.name == "example_project"


def test_module_name_shouldnt_have_file_extension(correct_project: Path):
    module_path = correct_project.joinpath("__init__.py")

    module = Module(module_path)

    assert module.name == "__init__"


def test_when_module_has_no_dependencies_should_return_empty_list(
    correct_project: Path,
):
    module_path = correct_project.joinpath("__init__.py")
    module = Module(module_path)

    dependencies = module.get_dependencies()

    assert dependencies == []


def test_when_module_has_python_dependencies_should_not_return_them(
    correct_project: Path,
):
    module_path = correct_project.joinpath("core", "services", "simple_service.py")
    module = Module(module_path)

    dependencies = module.get_dependencies()

    assert dependencies == []


def test_when_module_has_third_party_dependencies_should_not_return_them(
    correct_project: Path,
):
    module_path = correct_project.joinpath(
        "core", "services", "implementations", "simple_service.py"
    )
    module = Module(module_path)

    dependencies = module.get_dependencies()

    assert len(dependencies) == 1
    assert dependencies[0].names[0].name == "ISimpleService"


def test_when_module_has_dependencies_should_return_them(correct_project: Path):
    module_path = correct_project.joinpath("core", "use_cases", "simple_use_case.py")
    module = Module(module_path)

    dependencies = module.get_dependencies()

    assert len(dependencies) == 1

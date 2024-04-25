from pathlib import Path

from pytest import fixture

from arch_test.core.library import Library
from arch_test.core.python_dependency_parser import PythonDependencyParser

DATA_FOLDER_PATH = Path(__file__).parent.absolute().joinpath("data", "test_projects")


@fixture
def correct_project() -> Path:
    return DATA_FOLDER_PATH.joinpath("correct_project", "src", "example_project")


@fixture
def correct_project_library(correct_project: Path) -> Library:
    parser = PythonDependencyParser()
    return parser.parse(correct_project)

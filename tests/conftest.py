from pathlib import Path

from pytest import fixture

DATA_FOLDER_PATH = Path(__file__).parent.absolute().joinpath("data", "test_projects")


@fixture
def correct_project() -> Path:
    return DATA_FOLDER_PATH.joinpath("correct_project", "src", "example_project")

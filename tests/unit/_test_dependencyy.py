from pathlib import Path

from arch_test.core.dependencyy import find_project_root


def test_find_root_without_path_should_return_cwd():
    result = find_project_root()
    assert result == Path.cwd()


def test_find_root_with_path_should_return_project_root(correct_project):
    result = find_project_root(str(correct_project))
    assert result == correct_project

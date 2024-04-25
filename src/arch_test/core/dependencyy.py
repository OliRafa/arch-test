from __future__ import annotations

from pathlib import Path


def is_root_folder(src_path: Path) -> bool:
    if (
        (src_path / ".git").exists()
        or (src_path / ".hg").is_dir()
        or (src_path / "pyproject.toml").is_file()
    ):
        return True

    return False


def find_project_root(src_folder: str | None = None) -> Path:
    if not src_folder:
        src_path = Path.cwd().resolve()

    else:
        src_path = Path(src_folder).resolve()

    if is_root_folder(src_path):
        return src_path

    raise Exception()

from pathlib import Path


class Module:
    def __init__(self, path: Path) -> None:
        self.path = path

    @property
    def name(self) -> str:
        return self.path.name.replace(".py", "")

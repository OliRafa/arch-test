class PackageNotFoundError(Exception):
    "Raised when a Package wasn't found."

    def __init__(self, package_name: str, *args: object) -> None:
        super().__init__(*args)
        self.message = f"Package {package_name} wasn't found."


class ModuleNotFoundError(Exception):
    "Raised when a Module wasn't found."

    def __init__(self, module_name: str, *args: object) -> None:
        super().__init__(*args)
        self.message = f"Module {module_name} wasn't found."

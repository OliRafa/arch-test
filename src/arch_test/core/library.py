from arch_test.core.module import Module
from arch_test.core.package import Package


class Library:
    def __init__(self) -> None:
        self.packages: list[Package] = []
        self.modules: list[Module] = []


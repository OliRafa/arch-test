from tests.data.test_projects.correct_project.src.example_project.core.services.simple_service import (
    ISimpleService,
)


class ComplexUseCase:
    def __init__(self, simple_service: ISimpleService) -> None:
        self.simple_service = simple_service

    def execute(self): ...

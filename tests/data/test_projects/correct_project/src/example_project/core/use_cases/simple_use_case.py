from tests.data.test_projects.correct_project.src.example_project.services.simple_service import (
    SimpleService,
)


class SimpleUseCase:
    def __init__(self, simple_service: SimpleService) -> None:
        self.simple_service = simple_service

    def execute(self):
        ...

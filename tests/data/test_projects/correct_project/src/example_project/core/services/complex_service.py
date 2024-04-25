from abc import ABC, abstractmethod

from tests.data.test_projects.correct_project.src.example_project.core.services.simple_service import (
    ISimpleService,
)


class IComplexService(ISimpleService, ABC):

    @abstractmethod
    def get_something_complex(self): ...

import requests

from tests.data.test_projects.correct_project.src.example_project.core.services.simple_service import (
    ISimpleService,
)


class SimpleService(ISimpleService):
    def get_something_simple(self):
        something = requests.get()
        return something

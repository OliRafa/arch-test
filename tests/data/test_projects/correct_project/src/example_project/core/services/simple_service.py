from abc import ABC, abstractmethod


class ISimpleService(ABC):

    @abstractmethod
    def get_something_simple(self): ...

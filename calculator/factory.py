from abc import ABC, abstractmethod

class CommandFactory(ABC):
    @abstractmethod
    def create_command(self, calculator):
        pass

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class CommandFactory(ABC):
    @abstractmethod
    def create_command(self, calculator):
        pass

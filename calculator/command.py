"""
Module for defining the Command and CommandFactory abstract base classes.
"""

from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract base class for commands to be executed in the calculator application.
    """

    @abstractmethod
    def execute(self, *args):
        """
        Execute the command with the given arguments.

        Args:
            *args: The arguments required to execute the command.
        """

class CommandFactory(ABC):
    """
    Abstract base class for creating command instances.
    """

    @abstractmethod
    def create_command(self, calculator):
        """
        Create and return a command instance.

        Args:
            calculator (Calculator): The calculator instance to be used by the command.

        Returns:
            Command: A command instance.
        """

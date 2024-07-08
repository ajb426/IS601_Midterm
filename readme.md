# Midterm Calculator Application

## Overview

This calculator application is a robust and extensible calculator system designed to support various arithmetic operations and handle calculation history. This application is built using Python and implements several design patterns to ensure scalability, maintainability, and testability.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- Command-based architecture for extensibility.
- Persistent calculation history using Pandas.
- REPL (Read-Eval-Print Loop) interface for interactive use.
- Plugin system for adding new commands without modifying the core code.
- Detailed logging for monitoring and debugging.
- Thorough testing using Pytest and Github Actions to make sure all code is functioning as intended.

## Setup Instructions

### Prerequisites

- Python 3.10+
- `pip` (Python package installer)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ajb426/IS601_Midterm.git
```

2. Create and activate virutal environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file in the project root directory specifying the following variables:

DEBUG=true
LOG_OUTPUT_PATH=logs/app.log

DEBUG can be set to true or false (case insensitive), if True you will see the log output displayed in the console, if False it will only save to the log file.
LOG_OUTPUT_PATH is the path in which the log file will be created and updated.

## Using The Calculator

To start the calculator execute the following command from the project root directory:
```bash
python -m calculator
```
The calculator has the following commands:

### Add Command
- **Syntax**: `add <float> <float>`
- **Description**: Adds two numbers
- **Example**: 
    Enter command: add 3 5
    Result: 8.0

### Subtract Command
- **Syntax**: `subtract <float> <float>`
- **Description**: Subtracts the second number from the first.
- **Example**: 
    Enter command: subtract 10 4
    Result: 6.0


### Multiply Command
- **Syntax**: `multiply <float> <float>`
- **Description**: Multiplies two numbers.
- **Example**:
    Enter command: multiply 4 2
    Result: 8.0

### Divide Command
- **Syntax**: `divide <float> <float>`
- **Description**: Divides the first number by the second. Throws an error if attempting to divide by zero.
- **Example**: 
    Enter command: divide 10 2
    Result: 5.0
    Enter command: divide 10 0
    Error: Cannot divide by zero

### Square Command
- **Syntax**: `square <float>`
- **Description**: Squares the given number.
- **Example**:
    Enter command: square 4
    Result: 16.0

### History Command
- **Syntax**: `history`
- **Description**: Displays the calculation history.
- **Example**:
    Enter command: history
    operation operand1 operand2 result
    0 + 3.0 5.0 8.0
    1 - 10.0 4.0 6.0
    2 * 4.0 2.0 8.0
    3 / 10.0 2.0 5.0
    4 square 4.0 NaN 16.0

### Clear History Command
- **Syntax**: `clearhistory`
- **Description**: Clears the calculation history.
- **Example**:
    Enter command: clearhistory
    (No output, history is cleared)

### Get Last Calculation Command
- **Syntax**: `getlastcalculation`
- **Description**: Retrieves the last calculation performed.
- **Example**:
    Enter command: getlastcalculation
    operation square
    operand1 4
    operand2 NaN
    result 16
    Name: 4, dtype: object

### Save History Command
- **Syntax**: `savehistory <file_path>`
- **Description**: Saves the calculation history to the specified CSV file.
- **Example**:
    savehistory history.csv
    (No output, history is saved to the file)

### Load History Command
- **Syntax**: `loadhistory <file_path>`
- **Description**: Loads the calculation history from the specified CSV file.
- **Example**:
    Enter command: loadhistory history.csv
    (No output, history is loaded from the file)

### Menu Command
- **Syntax**: `menu`
- **Description**: Displays a menu of available commands. The result of this command is displayed when the calculator is initalized.
- **Example**:
    Enter command: menu
    (Displays a list of available commands)

### Exit Command
- **Syntax**: `exit`
- **Description**: Exits the REPL.
- **Example**:
    Enter command: exit
    Exiting REPL...

## Architectural Decisions

### Design Patterns

Several different design patterns we're used to implement the various functionalities of this calculalor. 

#### Command Pattern
The provided code utilizes the Command Pattern design, which is a behavioral design pattern. This pattern encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations. It also provides support for undoable operations. At the core of the design, we have the `Command` interface, which defines the `execute` method that all concrete command classes must implement.

```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass
```
The concrete command classes implement the Command interface and define the actual behavior of the various operations. Each command class holds a reference to the Calculator object and invokes the appropriate method on it.
```python
class AddCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, x, y):
        return self.calculator.add(x, y)
```

#### Factory Pattern
In addition to the Command Pattern, the provided code also utilizes the Factory Pattern. This pattern defines an interface for creating an object but allows subclasses to alter the type of objects that will be created. The CommandFactory interface defines a method for creating command objects.

```python
from abc import ABC, abstractmethod

class CommandFactory(ABC):
    @abstractmethod
    def create_command(self, calculator):
        pass
```
The concrete factory classes implement the CommandFactory interface and are responsible for creating instances of the corresponding command classes.
```python
class AddCommandFactory(CommandFactory):
    def create_command(self, calculator):
        return AddCommand(calculator)
```

### Singleton Pattern
The Singleton Design Pattern is a creational design pattern that ensures a class has only one instance and provides a global point of access to that instance. This pattern is useful when exactly one object is needed to coordinate actions across the system. The `SingletonMeta` class is a metaclass used to implement the Singleton pattern. It ensures that only one instance of the `Calculator` class is created.

```python
class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
```

### Error Handling
For this calculator, we employ two common error handling strategies: "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP). The use of these two strategies help to prevent error in the application before they happen.

#### Look Before You Leap (LBYL)
LBYL is a coding style where you check for potential problems before attempting an operation. This approach can prevent errors by ensuring that all preconditions are met before executing the code. In the `Calculator` class, we use LBYL when performing division to ensure that division by zero does not occur.

```python
def divide(self, operand1, operand2):
    """
    Divide two numbers and store the result.

    Args:
        operand1 (float): The first number.
        operand2 (float): The second number.

    Returns:
        float: The result of dividing operand1 by operand2.

    Raises:
        ValueError: If operand2 is zero.
    """
    if operand2 == 0:
        raise ValueError("Cannot divide by zero")
    result = operand1 / operand2
    self._store_calculation("/", operand1, operand2, result)
    return result
```
#### Easier to Ask for Forgiveness than Permission (EAFP)
EAFP is a coding style that assumes the operation will generally work and catches exceptions if it does not. This approach can lead to cleaner and more readable code, especially when the expected failure is rare. In the CalculatorREPL class, we use EAFP when executing commands. The code attempts to execute the command and catches any exceptions that may occur, handling them gracefully.

```python 
if command_name in self.commands:
                command = self.commands[command_name]
                try:
                    result = command.execute(*args)
                    self._print_result(result)
                    logging.info("Executed command '%s' with args %s: Result %s",
                                 command_name, args, result)
                except Exception as e:  # pylint: disable=broad-exception-caught
                    logging.error("Error executing command '%s': %s", command_name, e)
                    print(f"Error: {e}")
            else:
                logging.warning("Unknown command: %s", command_name)
                print("Unknown command")
```

### Logging
The logging strategy is integrated within the command execution process. Each command logs its execution details, including the command name, arguments, and results. This allows for detailed tracking and debugging of the application's behavior. Logging being displayed in the output can be enabled or disabled from within the environment variables.

```python
def configure_logging(self, logging_config=None):
        """
        Configure logging for the application.

        Args:
            logging_config (dict, optional): A dictionary containing logging configuration.
                If None, the default configuration is used.
        """
        if logging_config is None:
            log_output_path = self.settings.get('LOG_OUTPUT_PATH', 'logs/app.log')
            log_dir = os.path.dirname(log_output_path)
            os.makedirs(log_dir, exist_ok=True)  # Ensure the log directory exists
            debug_mode = self.settings.get('DEBUG', 'false').lower() == 'true'

            logging_config = {
                'version': 1,
                'disable_existing_loggers': False,
                'formatters': {
                    'default': {
                        'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        'datefmt': '%Y-%m-%d %H:%M:%S',
                    },
                },
                'handlers': {
                    'file': {
                        'level': 'DEBUG',
                        'class': 'logging.handlers.RotatingFileHandler',
                        'formatter': 'default',
                        'filename': log_output_path,
                        'mode': 'a',
                        'maxBytes': 1048576,
                        'backupCount': 5,
                    },
                    'console': {
                        'level': 'DEBUG' if debug_mode else 'INFO',
                        'class': 'logging.StreamHandler',
                        'formatter': 'default',
                    },
                },
                'root': {
                    'level': 'DEBUG',
                    'handlers': ['file', 'console'] if debug_mode else ['file'],
                },
            }

        logging.config.dictConfig(logging_config)

        # Determine debug_mode based on logging_config
        debug_mode = logging_config['handlers'].get('console', {}).get('level') == 'DEBUG'

        logging.info("Logging configured. Debug mode: %s", debug_mode)
        logging.info("Log output path: %s", logging_config['handlers']['file']['filename'])
```

## Video Demonstration
Click here to see a video demonstration of the commands, environment variables, and logging: https://youtu.be/2tE0Xht-Mow

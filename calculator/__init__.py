import os
import logging
import logging.config
from dotenv import load_dotenv
from calculator.plugin_manager import PluginManager
from calculator.command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, GetHistoryCommand, ClearHistoryCommand, GetLastCalculationCommand, SaveHistoryCommand, LoadHistoryCommand
from calculator.calculator import Calculator
import warnings

warnings.filterwarnings("ignore", category=FutureWarning, message=".*DataFrame concatenation with empty or all-NA entries.*")

class CalculatorApp:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.configure_logging()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.calculator = Calculator()
        self.commands = self.initialize_default_commands()
        self.plugin_manager = PluginManager(self.commands, self.calculator)
        self.load_plugins()

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        return settings

    def configure_logging(self):
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

        logging.info("Logging configured. Debug mode: %s", debug_mode)
        logging.info("Log output path: %s", log_output_path)


    def initialize_default_commands(self):
        commands = {
           'add': AddCommand(self.calculator),
            'subtract': SubtractCommand(self.calculator),
            'multiply': MultiplyCommand(self.calculator),
            'divide': DivideCommand(self.calculator),
            'history': GetHistoryCommand(self.calculator),
            'clear_history': ClearHistoryCommand(self.calculator),
            'last': GetLastCalculationCommand(self.calculator),
            'save_history': SaveHistoryCommand(self.calculator),
            'load_history': LoadHistoryCommand(self.calculator)
        }
        logging.info("Default commands initialized: %s", list(commands.keys()))
        return commands

    def load_plugins(self):
        self.plugin_manager.load_plugins()

    def start_repl(self):
        from calculator.repl import CalculatorREPL
        repl = CalculatorREPL(self.commands)
        repl.start()

    def start(self):
        logging.info("Application started. Type 'exit' to exit.")
        self.start_repl()
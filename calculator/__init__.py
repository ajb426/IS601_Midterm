"""
This module initializes the Calculator application, loads environment variables,
configures logging, loads plugins, and starts the REPL.
"""

import os
import warnings
import logging
import logging.config
from dotenv import load_dotenv
from calculator.plugin_manager import PluginManager
from calculator.calculator import Calculator
from calculator.repl import CalculatorREPL

warnings.filterwarnings("ignore", category=FutureWarning,
                        message=".*DataFrame concatenation with empty or all-NA entries.*")

class CalculatorApp:
    """Represents the Calculator application."""

    def __init__(self):
        """Initialize the Calculator application."""
        os.makedirs('logs', exist_ok=True)
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.configure_logging()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.calculator = Calculator()
        self.commands = {}
        self.plugin_manager = PluginManager(self.commands, self.calculator)
        self.load_plugins()

    def load_environment_variables(self):
        """
        Load environment variables into a dictionary.

        Returns:
            dict: A dictionary containing environment variables.
        """
        return dict(os.environ.items())

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

    def load_plugins(self):
        """Load command plugins."""
        self.plugin_manager.load_plugins()

    def start_repl(self):
        """Start the REPL (Read-Eval-Print Loop)."""
        repl = CalculatorREPL(self.commands)
        repl.start()

    def start(self):
        """Start the application."""
        logging.info("Application started. Type 'exit' to exit.")
        self.start_repl()

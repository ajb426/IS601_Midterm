import logging
import pytest
from calculator import CalculatorApp
from unittest.mock import patch

@pytest.fixture
def setup_environment():
    return 'logs/app_test.log'

@pytest.fixture
def logging_config():
    return {
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
                'filename': 'logs/app_test.log',
                'mode': 'a',
                'maxBytes': 1048576,
                'backupCount': 5,
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['file', 'console'],
        },
    }

def test_configure_logging(setup_environment, logging_config):
    app = CalculatorApp()
    app.configure_logging(logging_config=logging_config)

    logger = logging.getLogger()
    logger.debug('Test debug message')

    # Check the log file for the expected log message
    with open(setup_environment, 'r') as log_file:
        log_content = log_file.read()

    assert 'Test debug message' in log_content

@patch.object(CalculatorApp, 'start_repl', lambda x: None)
def test_start(setup_environment, logging_config):
    app = CalculatorApp()
    app.configure_logging(logging_config=logging_config)
    app.start()

    # Check the log file for the expected log message
    with open(setup_environment, 'r') as log_file:
        log_content = log_file.read()

    assert 'Application started. Type \'exit\' to exit.' in log_content

"""
This module manages the history of calculations, including saving to and loading from a CSV file.
"""

import os
import pandas as pd
from calculator.calculation import Calculation

class CalculatorHistory:
    """
    Manages the history of calculations, including saving to and loading from a CSV file.
    """

    def __init__(self, file_path='history.csv'):
        """
        Initialize the CalculatorHistory.

        Args:
            file_path (str): The path to the CSV file where the history is stored. 
            Defaults to 'history.csv'.
        """
        self.file_path = file_path
        self.df = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])

    def load_from_csv(self):
        """
        Load calculation history from a CSV file.
        """
        if os.path.exists(self.file_path):
            self.df = pd.read_csv(self.file_path)
        else:
            self.df = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])

    def save_to_csv(self):
        """
        Save the current calculation history to a CSV file.
        """
        self.df.to_csv(self.file_path, index=False)

    def add_record(self, calculation):
        """
        Add a new calculation record to the history.

        Args:
            calculation (Calculation): An instance of the Calculation class 
            containing the operation details.
        """
        new_record = pd.DataFrame(
            [[calculation.operation,
              calculation.operand1,
              calculation.operand2,
              calculation.result]],
            columns=['operation', 'operand1', 'operand2', 'result']
        )
        self.df = pd.concat([self.df, new_record], ignore_index=True)

    def clear_history(self):
        """
        Clear the calculation history.
        """
        self.df = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])

    def get_last_record(self):
        """
        Get the last calculation record from the history.

        Returns:
            Calculation: The last calculation record, or None if the history is empty.
        """
        if not self.df.empty:
            last_row = self.df.iloc[-1]
            return Calculation(last_row['operation'],
                               last_row['operand1'],
                               last_row['operand2'],
                               last_row['result'])
        return None

    def get_all_records(self):
        """
        Get all calculation records from the history.

        Returns:
            DataFrame: A DataFrame containing all calculation records.
        """
        return self.df

    def set_file_path(self, file_path):
        """
        Set the file path for the CSV file where the history is stored.

        Args:
            file_path (str): The new file path.
        """
        self.file_path = file_path

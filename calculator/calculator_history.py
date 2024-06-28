import pandas as pd
import os
from calculator.calculation import Calculation

class CalculatorHistory:
    def __init__(self, file_path='history.csv'):
        self.file_path = file_path
        self.df = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])

    def load_from_csv(self):
        if os.path.exists(self.file_path):
            self.df = pd.read_csv(self.file_path)
        else:
            self.df = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])

    def save_to_csv(self):
        self.df.to_csv(self.file_path, index=False)

    def add_record(self, calculation):
        new_record = pd.DataFrame([[calculation.operation, calculation.operand1, calculation.operand2, calculation.result]], columns=['operation', 'operand1', 'operand2', 'result'])
        self.df = pd.concat([self.df, new_record], ignore_index=True)

    def clear_history(self):
        self.df = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])

    def get_last_record(self):
        if not self.df.empty:
            last_row = self.df.iloc[-1]
            return Calculation(last_row['operation'], last_row['operand1'], last_row['operand2'], last_row['result'])
        return None

    def get_all_records(self):
        return self.df

    def set_file_path(self, file_path):
        self.file_path = file_path

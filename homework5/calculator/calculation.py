class Calculation:
    """
    A class to represent a single calculation.
    """
    def __init__(self, operation, x, y, result):
        self.operation = operation
        self.x = x
        self.y = y
        self.result = result

    def __repr__(self):
        return f"{self.x} {self.operation} {self.y} = {self.result}"

    def get_details(self):
        return (self.operation, self.x, self.y, self.result)

class Calculator:
    def __init__(self):
        self.result = None

    def add_values(self, a, b):
        self.result = a + b
        self.print_result("dodawania")

    def sub_values(self, a, b):
        self.result = a - b
        self.print_result("odejmowania")

    def print_result(self, operation: str):
        print("Wynikiem {} jest {}".
              format(operation, self.result))

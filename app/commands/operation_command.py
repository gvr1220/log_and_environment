from app.commands import Command
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.input_handler import get_user_input

class OperationCommand(Command):
    def __init__(self, operation_function):
        self.operation_function = operation_function

    def execute(self):
        a, b = get_user_input()
        try:
            result = self.operation_function(a, b)
            calculation = Calculation.create(a, b, self.operation_function)
            Calculations.add_calculation(calculation)
            print("The result of {} operation is {}".format(self.operation_function.__name__, result))
        except ValueError as e:
            print(e)
            print("Please enter a non-zero divisor.")
from app.commands import CommandHandler
from app.plugins.add import AddCommand
from app.plugins.divide import DivideCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.menu import MenuCommand
from app.plugins.exit import ExitCommand


class App:
    def __init__(self):  # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        # Register commands here
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("exit", ExitCommand())

        print("Type 'exit' to exit.")
        while True:  # REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())

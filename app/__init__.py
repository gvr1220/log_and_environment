from app.commands import CommandHandler
from app.plugin.add import AddCommand
from app.plugin.divide import DivideCommand
from app.plugin.multiply import MultiplyCommand
from app.plugin.subtract import SubtractCommand
from app.plugin.menu import MenuCommand
from app.plugin.exit import ExitCommand


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

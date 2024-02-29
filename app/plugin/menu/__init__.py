import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        print("Displaying menu:")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
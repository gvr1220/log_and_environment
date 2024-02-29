"""
Module docstring: This module contains unit tests for the App class and its commands.
"""

import pytest
from app import App
from app.plugins.add import AddCommand
from app.plugins.divide import DivideCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand

def test_add_command(capfd):
    """Test the AddCommand."""
    app = App()
    app.command_handler.register_command("add", AddCommand())
    app.command_handler.execute_command("add")
    captured = capfd.readouterr()  # Capture the printed output
    assert captured.out.strip() == "Executing addition command"

def test_divide_command(capfd):
    """Test the DivideCommand."""
    app = App()
    app.command_handler.register_command("divide", DivideCommand())
    app.command_handler.execute_command("divide")
    captured = capfd.readouterr()
    assert captured.out.strip() == "Executing division command"

def test_subtract_command(capfd):
    """Test the SubtractCommand."""
    app = App()
    app.command_handler.register_command("subtract", SubtractCommand())
    app.command_handler.execute_command("subtract")
    captured = capfd.readouterr()
    assert captured.out.strip() == "Executing subtraction command"

def test_multiply_command(capfd):
    """Test the MultiplyCommand."""
    app = App()
    app.command_handler.register_command("multiply", MultiplyCommand())
    app.command_handler.execute_command("multiply")
    captured = capfd.readouterr()  # Capture the printed output
    assert captured.out.strip() == "Executing multiplication command"

def test_app_exit(capfd, monkeypatch):
    """Test that the app exits properly."""
    inputs = iter(['exit'])  # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the app menu command works."""
    # Simulate user entering 'menu' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

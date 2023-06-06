# Here is testing for the createPlayers.py file
# I'm having issues with this:
# from src.package import createPlayers 
# ModuleNotFoundError: No module named 'src'
from src import createPlayers


def test_createPlayers():
    assert createPlayers.playerCreation(2, "a", "b") == 1


# Personal Note: run: python -m package.tests.test_createPlayers 
# from top level
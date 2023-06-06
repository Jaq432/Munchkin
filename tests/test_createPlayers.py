# Here is testing for the createPlayers.py file

from src import createPlayers


def test_createPlayers():
    assert createPlayers.playerCreation(2, "a", "b") == 1

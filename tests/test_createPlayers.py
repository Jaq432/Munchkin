import pytest

from createPlayers import \
    createPlayers

def test_createPlayers():
    assert createPlayers(2,"a","b") == 1
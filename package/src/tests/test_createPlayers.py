# Here is testing for the createPlayers.py file
# I'm having issues with this:
# from src.package import createPlayers
# ModuleNotFoundError: No module named 'src'
from src.Types import player
from src.Types import weapon
from src.Types import item

def test_createPlayers():
    testWeapon = weapon.Weapon("Iron Claymore","2 hand",2,200,"Clunky but effective",25)
    testItem = item.Item("Basic Helmet","head",1,50,"Better than nothing (leather)",50)
    testCard = item.Item("Basic Helmet","head",1,50,"Better than nothing (leather)",50)

    testPlayer = player.Player(
        "TestBob",
        1,
        ["human"],
        ["cleric"],
        [testWeapon],
        [testItem],
        1,
        [testCard],
    )

    assert isinstance(testPlayer, player.Player) == True

# Personal Note: run: python -m package.tests.test_createPlayers 
# from top level

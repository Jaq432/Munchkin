import src.Types.player as player
import src.Types.weapon as weapon
import src.Types.item as item

# Tests player creation with all fields populated
def test_createPlayers():
    testPlayer = player.Player("TestBob",1,[],[],[],[],1,[])
    assert isinstance(testPlayer, player.Player) == True

def test_updatePlayerName():
    testPlayer = player.Player("TestBob", 1, ["human"], ["cleric"], [], [], 1, [])
    testPlayer.setName("TestFred")
    assert testPlayer.getName() == "TestFred"

def test_updatePlayerLevel():
    testPlayer = player.Player("TestBob", 1, ["human"], ["cleric"], [], [], 1, [])
    testPlayer.setLevel(2)
    assert testPlayer.getLevel() == 2

def test_updatePlayerRace():
    testPlayer = player.Player("TestBob", 1, ["human"], ["cleric"], [], [], 1, [])
    testPlayer.setRace("dwarf")
    assert testPlayer.getRace() == "dwarf"

def test_updatePlayerWeapon():
    testPlayer = player.Player("TestBob", 1, ["human"], ["cleric"], [], [], 1, [])
    testWeapon = weapon.Weapon("Iron Claymore","2 hand",2,200,"Clunky but effective",25)
    testPlayer.setWeapon(testWeapon)
    assert testPlayer.getWeapons() == [testWeapon]

def test_updatePlayerItems():
    testPlayer = player.Player("TestBob", 1, ["human"], ["cleric"], [], [], 1, [])
    testItem = item.Item("Basic Helmet","head",1,50,"Better than nothing (leather)",50)
    testPlayer.setItems(testItem)
    assert testPlayer.getItems() == [testItem]

def test_updatePlayerCards():
    testPlayer = player.Player("TestBob", 1, ["human"], ["cleric"], [], [], 1, [])
    testCard = item.Item("Basic Helmet","head",1,50,"Better than nothing (leather)",50)
    testPlayer.setCardsInHand(testCard)
    assert testPlayer.getCardsInHand() == [testCard]
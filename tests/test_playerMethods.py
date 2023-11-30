import src.Types.classes as classes
import src.Types.item as item
import src.Types.player as player
import src.Types.weapon as weapon

testClass = classes.Class("Barbarian",250,"dual wield",10)
testPlayer = player.Player("TestBob", 1, ["human"], testClass, [], [], 1, [], 0)
testItem = item.Item("Basic Helmet","head",1,50,"Better than nothing (leather)",50)
testWeapon = weapon.Weapon("Wood Shortsword","1 hand",1,50,"Better than nothing",50)

def test_createPlayers():
    assert isinstance(testPlayer, player.Player) == True

def test_updatePlayerName():
    testPlayer.setName("TestFred")
    assert testPlayer.getName() == "TestFred"

def test_updatePlayerLevel():
    testPlayer.setLevel(2)
    assert testPlayer.getLevel() == 2

def test_updatePlayerRace():
    testPlayer.setRace("dwarf")
    assert testPlayer.getRace() == "dwarf"

def test_updatePlayerClass():
    testPlayer.setClass(testClass)
    assert testPlayer.getClass()[0].getName() == "Barbarian"

def test_updatePlayerWeapon():
    testPlayer.setWeapon(testWeapon)
    assert testPlayer.getWeapons() == [testWeapon]

def test_updatePlayerItems():
    testPlayer.setItems(testItem)
    assert testPlayer.getItems() == [testItem]

def test_updatePlayerCards():
    testPlayer.addCardToHand(testItem)
    assert testPlayer.getCardsInHand() == [testItem]

def test_sellPlayerEquippedWeapon():
    testPlayer.setGold = 0
    testPlayer.setWeapon(testWeapon)
    testPlayer.sellEquippedCard(testWeapon)
    assert testPlayer.getGold() == 50

def test_sellPlayerEquippedItem():
    testPlayer.setGold = 0
    testPlayer.setItems(testItem)
    testPlayer.sellEquippedCard(testItem)
    assert testPlayer.getGold() == 50

def test_sellPlayerEquippedClass():
    testPlayer.setGold = 0
    testPlayer.setClass(testClass)
    testPlayer.sellEquippedCard(testClass)
    assert testPlayer.getGold() == 250

def test_sellPlayerHandWeapon():
    testPlayer.setGold = 0
    testPlayer.addCardToHand(testWeapon)
    testPlayer.sellHandCard(testWeapon)
    assert testPlayer.getGold() == 50

def test_sellPlayerHandItem():
    testPlayer.setGold = 0
    testPlayer.addCardToHand(testItem)
    testPlayer.sellHandCard(testItem)
    assert testPlayer.getGold() == 50

def test_sellPlayerHandClass():
    testPlayer.setGold = 0
    testPlayer.addCardToHand(testClass)
    testPlayer.sellHandCard(testClass)
    assert testPlayer.getGold() == 250
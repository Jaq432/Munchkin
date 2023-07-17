import src.Types.item as item

def test_createItem():
    testItem = item.Item("Basic Helmet","head",1,50,"Better than nothing (leather)",50)
    assert isinstance(testItem, item.Item) == True

def test_updateItemName():
    testItem = item.Item("Basic Helmet","head",1,50,"Better than nothing (leather)",50)
    testItem.setName("TestFred")
    assert testItem.getName() == "TestFred"

def test_updateItemAttack():
    testItem = item.Item("Basic Helmet","head",1,50,"Better than nothing (leather)",50)
    testItem.setAttack(99)
    assert testItem.getAttack() == 99

def test_updateItemCost():
    testItem = item.Item("Basic Helmet","head",1,50,"Better than nothing (leather)",50)
    testItem.setCost(99)
    assert testItem.getCost() == 99

def test_updateItemSpecialProperties():
    testItem = item.Item("Basic Helmet","head",1,50,"Better than nothing (leather)",50)
    testItem.setSpecialProperties("TestFred")
    assert testItem.getSpecialProperties() == "TestFred"

def test_updateItemType():
    testItem = item.Item("Basic Helmet","head",1,50,"Better than nothing (leather)",50)
    testItem.setType("TestFred")
    assert testItem.getType() == "TestFred"

def test_updateItemDropChance():
    testItem = item.Item("Basic Helmet","head",1,50,"Better than nothing (leather)",50)
    testItem.setDropChance(99)
    assert testItem.getDropChance() == 99

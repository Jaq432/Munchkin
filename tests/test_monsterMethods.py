import src.Types.monster as monster

# Boar,animal,1,Just a boar,1,1,50
def test_createMonster():
    testMonster = monster.Monster("Boar","animal",1,"Just a boar",1,1,50)
    assert isinstance(testMonster, monster.Monster) == True

def test_updateMonsterName():
    testMonster = monster.Monster("Boar","animal",1,"Just a boar",1,1,50)
    testMonster.setName("TestFred")
    assert testMonster.getName() == "TestFred"

def test_updateMonsterType():
    testMonster = monster.Monster("Boar","animal",1,"Just a boar",1,1,50)
    testMonster.setType("undead")
    assert testMonster.getType() == "undead"

def test_updateMonsterAttack():
    testMonster = monster.Monster("Boar","animal",1,"Just a boar",1,1,50)
    testMonster.setAttack(99)
    assert testMonster.getAttack() == 99

def test_updateMonsterDescription():
    testMonster = monster.Monster("Boar","animal",1,"Just a boar",1,1,50)
    testMonster.setDescription("More than a boar")
    assert testMonster.getDescription() == "More than a boar"

def test_updateMonsterLevelsGain():
    testMonster = monster.Monster("Boar","animal",1,"Just a boar",1,1,50)
    testMonster.setLevelsGain(99)
    assert testMonster.getLevelsGain() == 99

def test_updateMonsterLootGain():
    testMonster = monster.Monster("Boar","animal",1,"Just a boar",1,1,50)
    testMonster.setLootGain(99)
    assert testMonster.getLootGain() == 99

def test_updateMonsterSpawnChance():
    testMonster = monster.Monster("Boar","animal",1,"Just a boar",1,1,50)
    testMonster.setSpawnChance(99)
    assert testMonster.getSpawnChance() == 99
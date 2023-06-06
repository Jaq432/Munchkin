import Types.item as item
import Types.weapon as weapon
import Types.monster as monster

def initialize():
    # Initialize the tables of items, weapons, and mosnters
    itemsFile = open("src/Resources/items.csv","r")
    weaponsFile = open("src/Resources/weapons.csv","r")
    monstersFile = open("src/Resources/monsters.csv","r")

    itemsTable = []
    weaponsTable = []
    monstersTable = []

    for line in itemsFile:
        if line[0] == "#":
            continue
        else: 
            line = line.split(",")
            # itemName,itemType,itemAttack,itemCost,itemSpecialProperties
            itemsTable.append(item.Item(line[0], line[1], line[2], line[3], line[4]))
    
    for line in weaponsFile:
        if line[0] == "#":
            continue
        else: 
            line = line.split(",")
            # weaponName,weaponType,weaponAttack,weaponCost,weaponSpecialProperties
            weaponsTable.append(weapon.Weapon(line[0], line[1], line[2], line[3], line[4]))

    for line in monstersFile:
        if line[0] == "#":
            continue
        else: 
            line = line.split(",")
            # monsterName,monsterType,monsterAttack,monsterDescription,monsterLevelsGain,monsterLootGain
            monstersTable.append(monster.Monster(line[0], line[1], line[2], line[3], line[4], line[5]))

    # Clean up our tracks
    itemsFile.close()
    weaponsFile.close()
    monstersFile.close()

    return itemsTable, weaponsTable, monstersTable
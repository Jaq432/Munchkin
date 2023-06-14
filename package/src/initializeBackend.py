import os

import Types.item as item
import Types.weapon as weapon
import Types.monster as monster


def initialize():
    # Get the working directory
    dirname = os.path.dirname(__file__)

    # Initialize the tables of items, weapons, and mosnters
    # The value of "nt" is for windows which references files differently
    if str(os.name) == "nt":
        itemsDirectory = dirname + "\\Resources\\items.csv"
        weaponsDirectory = dirname + "\\Resources\\weapons.csv"
        monsterDirectory = dirname + "\\Resources\\monsters.csv"
    # If not nt, it is linux/mac based and needs different a directory format
    else:
        itemsDirectory = dirname + "/Resources/items.csv"
        weaponsDirectory = dirname + "/Resources/weapons.csv"
        monsterDirectory = dirname + "/Resources/monsters.csv"

    itemsFile = open(itemsDirectory, "r")
    weaponsFile = open(weaponsDirectory, "r")
    monstersFile = open(monsterDirectory, "r")

    itemsTable = []
    weaponsTable = []
    monstersTable = []

    for line in itemsFile:
        if line[0] == "#":
            continue

        else:
            line = line.split(",")
            # itemName,itemType,itemAttack,itemCost,itemSpecialProperties,lootDropChance
            newItem = item.Item(line[0], line[1], line[2], line[3], line[4], line[5])
            itemsTable.append(newItem)

    for line in weaponsFile:
        if line[0] == "#":
            continue

        else:
            line = line.split(",")
            # weaponName,weaponType,weaponAttack,weaponCost,weaponSpecialProperties,lootDropChance
            newWeapon = weapon.Weapon(line[0], line[1], line[2], line[3], line[4], line[5])
            weaponsTable.append(newWeapon)

    for line in monstersFile:
        if line[0] == "#":
            continue

        else:
            line = line.split(",")
            # monsterName,monsterType,monsterAttack,monsterDescription,monsterLevelsGain,monsterLootGain,monsterSpawnChance
            newMonster = monster.Monster(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
            monstersTable.append(newMonster)

    # Clean up our tracks
    itemsFile.close()
    weaponsFile.close()
    monstersFile.close()

    return itemsTable, weaponsTable, monstersTable

import os

import Types.item as item
import Types.weapon as weapon
import Types.monster as monster
import Types.classes as classes


def initialize():
    # Get the working directory
    dirname = os.path.dirname(__file__)

    # Initialize the tables of items, weapons, and mosnters
    # The value of "nt" is for windows which references files differently
    if str(os.name) == "nt":
        itemsDirectory = dirname + "\\Resources\\items.csv"
        weaponsDirectory = dirname + "\\Resources\\weapons.csv"
        monsterDirectory = dirname + "\\Resources\\monsters.csv"
        classesDirectory = dirname + "\\Resources\\classes.csv"
    # If not nt, it is linux/mac based and needs different a directory format
    else:
        itemsDirectory = dirname + "/Resources/items.csv"
        weaponsDirectory = dirname + "/Resources/weapons.csv"
        monsterDirectory = dirname + "/Resources/monsters.csv"
        classesDirectory = dirname + "/Resources/classes.csv"

    itemsFile = open(itemsDirectory, "r")
    weaponsFile = open(weaponsDirectory, "r")
    monstersFile = open(monsterDirectory, "r")
    classesFile = open(classesDirectory, 'r')

    itemsTable = []
    weaponsTable = []
    monstersTable = []
    classesTable = []

    for line in itemsFile:
        if line[0] == "#":
            continue

        else:
            # Pull out and scrub each field
            line = line.split(",")
            itemName = str(line[0])
            itemType = str(line[1])
            itemAttack = int(line[2])
            itemCost = int(line[3])
            itemSpecialProperties = str(line[4])
            itemDropChance = int(line[5])

            # Create and add it to the table
            newItem = item.Item(
                itemName,
                itemType,
                itemAttack,
                itemCost,
                itemSpecialProperties,
                itemDropChance,
            )
            itemsTable.append(newItem)

    for line in weaponsFile:
        if line[0] == "#":
            continue

        else:
            # Pull out and scrub each field
            line = line.split(",")
            weaponName = str(line[0])
            weaponType = str(line[1])
            weaponAttack = int(line[2])
            weaponCost = int(line[3])
            weaponSpecialProperties = str(line[4])
            weaponDropChance = int(line[5])

            # Create and add it to the table
            newWeapon = weapon.Weapon(
                weaponName,
                weaponType,
                weaponAttack,
                weaponCost,
                weaponSpecialProperties,
                weaponDropChance,
            )
            weaponsTable.append(newWeapon)

    for line in monstersFile:
        if line[0] == "#":
            continue

        else:
            # Pull out and scrub each field
            line = line.split(",")
            monsterName = str(line[0])
            monsterType = str(line[1])
            monsterAttack = int(line[2])
            monsterDescription = str(line[3])
            monsterLevelsGain = int(line[4])
            monsterLootGain = int(line[5])
            monsterSpawnChance = int(line[6])

            # Create and add it to the table
            newMonster = monster.Monster(
                monsterName,
                monsterType,
                monsterAttack,
                monsterDescription,
                monsterLevelsGain,
                monsterLootGain,
                monsterSpawnChance,
            )
            monstersTable.append(newMonster)

        for line in classesFile:
            if line[0] == "#":
                continue

            else:
                # Pull out and scrub each field
                line = line.split(",")
                className = str(line[0])
                classcost = int(line[1])
                classSpecialProperties = str(line[2])
                classDropChanceWeight = int(line[3])

                # Create and add it to the table
                newClass = classes.Class(
                    className,
                    classcost,
                    classSpecialProperties,
                    classDropChanceWeight,
                )
                classesTable.append(newMonster)

    # Clean up our tracks
    itemsFile.close()
    weaponsFile.close()
    monstersFile.close()

    return itemsTable, weaponsTable, monstersTable

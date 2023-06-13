# public imports
import time
import random
import os

# private imports
import Types.monster as monster
import UserInterfaces.combatTextInterface as combatTextInterface


# The main function of the game
# We want to kick in the door, roll odds and either proceed with a monster or loot encounter
def kickInDoor(player, lootTable):
    print("Kicking in the door.")
    # May the odds be in your favor
    decidingValue = random.randint(1, 10)
    if decidingValue == 10: 
        print("You encountered an item. Looting the room.")
        time.sleep(1)
        # Create a dummy monster to pass in which has a loot value of 1 and level gain of 0
        dummyMonster = monster.Monster(
            "DoorMonster", "chest", 0, "Kick in door loot dummy", 0, 1
        )
        lootTheRoom(player, dummyMonster, lootTable)  # This is where I left off.
    # Encounter a monster
    else:
        # Get the number of lines in the monsters data file
        # Get the working directory
        dirname = os.path.dirname(__file__)

        # The value of "nt" is for windows which references files differently
        if str(os.name) == "nt":
            monsterDirectory = dirname + "\\Resources\\monsters.csv"

        else:
            monsterDirectory = dirname + "/Resources/monsters.csv"

        monsterFile = open(monsterDirectory, "r")

        # Get a count of the lines in the file representing monsters
        numOfMonsterLines = 0
        for monsterLine in monsterFile:
            numOfMonsterLines += 1

        # Closing the file so that I can reopen it later
        monsterFile.close()

        # Choose a random monster number to get
        monsterValue = random.randint(1, numOfMonsterLines)

        # Reopening the monster file
        monsterFile = open(monsterDirectory, "r")

        lineCount = 0
        for monsterLine in monsterFile:
            # Found the monster we are looking for
            if lineCount == monsterValue:
                monsterAttributes = monsterLine.split(",")
                # Do the fight and pass in the monster
                doorMonster = monster.Monster(
                    monsterAttributes[0],
                    monsterAttributes[1],
                    monsterAttributes[2],
                    monsterAttributes[3],
                    monsterAttributes[4],
                    monsterAttributes[5],
                )
                print("You encountered a " + str(doorMonster.getName()) + "!")
                combatTextInterface.MainConsole(player, doorMonster, lootTable)
                break
            # Didn't find the monster we are looking for
            if lineCount == numOfMonsterLines:
                print(
                    "We reached the end of the monster file without finding the assigned monster. \
                        Something went wrong."
                )
                break
            # Increment to look at the next line
            lineCount += 1
'''
dropTable = {
    'Leather Item': 50, #50% chance
    'Iron Item': 25, #25% chance
    'Steel Item': 10 #10% chance
}

# Function to perform weighted random selection
def weighted_random_selection(drop_table):
    total_weight = sum(drop_table.values())
    rand_num = random.uniform(0, total_weight)
    current_weight = 0

    for item, weight in drop_table.items():
        current_weight += weight
        if rand_num <= current_weight:
            return item

# Example usage
for _ in range(10):
    dropped_item = weighted_random_selection(drop_table)
    print("Dropped item:", dropped_item)
'''
def lootTheRoom(player, monster, lootTable):
    # Get the total value of weighted drop chance = 340 as of writing
    totalDropChanceWeight = 0
    for item in lootTable:
        totalDropChanceWeight += item.getDropChance()

    for i in range(monster.getLootGain()):
        # This reperesents the index of the random item that we will loot
        randomSelector = random.randint(0, totalDropChanceWeight)
        index = 0
        for item in lootTable:
            if index == randomSelector:
                player.setCardsInHand(lootTable[randomSelector])
                print("The hero looted: " + str(lootTable[randomSelector].getName()))
                index += 1
                continue


def fight(player, monster):
    if player.getAttack() >= monster.getAttack():
        print("You won the battle! Loot the room.")
        lootTheRoom(player, monster)
    else:
        print("You can't fight the monster since you are weaker.")
        time.sleep(1)
        print(
            "Either equip items to make yourself stronger, ask for assistance, or run."
        )


def run(player, monster):
    print("Running from the monster. Losing a level.")
    player.setLeve(player.getLevel() - 1)


def equipWeapon(player, weapon):
    player.setWeapon(weapon)


def equipItem(player, item):
    player.set(item)


def unequipWeapon(player, weapon):
    player.deleteWeapon(weapon)

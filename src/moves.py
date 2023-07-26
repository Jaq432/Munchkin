# public imports
import time
import random
import os

# private imports
import Types.monster as monster
import UserInterfaces.combatTextInterface as combatTextInterface


# The main function of the game
# We want to kick in the door, roll odds and either proceed with a monster or loot encounter
def kickInDoor(player, monsterTable, lootTable):
    print("Kicking in the door.")
    # May the odds be in your favor
    decidingValue = random.randint(1, 10)
    if decidingValue == 10: 
        print("You encountered an item. Looting the room.")
        time.sleep(1)
        # Create a dummy monster to pass in which has a loot value of 1 and level gain of 0
        dummyMonster = monster.Monster(
            "DoorMonster", "chest", 0, "Kick in door loot dummy", 0, 1,1
        )
        lootTheRoom(player, dummyMonster, lootTable)
    # Encounter a monster
    else:
        # Get a total count of the possible spawn rate
        totalSpawnChanceWeight = 0
        for monster in monsterTable:
            totalSpawnChanceWeight += monster.getSpawnChance()

        # Choose a random monster number to get
        monsterValue = random.randint(0, totalSpawnChanceWeight)

        weightedSum = 0
        for monster in monsterTable:
            weightedSum += monster.getSpawnChance()
            if weightedSum >= monsterValue:
                print("You encountered a " + str(monster.getName()))
                combatTextInterface.MainConsole(player, monster, lootTable)
                break

def lootTheRoom(player, monster, lootTable):
    # Get the total value of weighted drop chance = 500+ as of writing
    totalDropChanceWeight = 0
    for item in lootTable:
        totalDropChanceWeight += item.getDropChance()

    # Get x number of loot based on the monster
    for i in range(monster.getLootGain()):
        # This reperesents the index of the random item that we will loot
        randomSelector = random.randint(0, totalDropChanceWeight)
        weightedSum = 0
        for item in lootTable:
            weightedSum += item.getDropChance()
            if weightedSum >= randomSelector:
                player.addCardToHand(item)
                print("The hero looted: " + str(item.getName()))
                break


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


def equipWeapon(player, weapon):
    player.setWeapon(weapon)


def equipItem(player, item):
    player.set(item)


def unequipWeapon(player, weapon):
    player.deleteEquippedWeapon(weapon)

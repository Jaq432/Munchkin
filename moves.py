# public imports
import time
import random

# private imports
import Types.monster as monster
import UserInterfaces.combatTextInterface as combatTextInterface

# The main function of the game
# We want to kick in the door, roll odds and either proceed with a monster or loot encounter
def kickInDoor(player,lootTable):
    print("Kicking in the door.")
    # May the odds be in your favor
    decidingValue = random.randint(1,10)
    if decidingValue == 10:
        print("You encountered an item. Looting the room.")
        time.sleep(1)
        # Create a dummy monster to pass in which has a loot value of 1 and level gain of 0
        dummyMonster = monster.Monster("DoorMonster","chest",0,"Kick in door loot dummy",0,1)
        lootTheRoom(player,dummyMonster,lootTable) # This is where I left off.
    else:
        print("You encountered a monster.")
        # TODO: get a random monster from the monster table
        # Get the number of lines in the monsters data file
        monsterFile = open("Resources\monsters.csv", "r")
        
        # Get a count of the lines in the file representing monsters
        numOfMonsterLines = 0
        for monsterLine in monsterFile:
            numOfMonsterLines += 1

        monsterValue = random.randint(1,numOfMonsterLines)

        lineCount = 0
        for monsterLine in monsterFile:
            # Found the monster we are looking for
            if lineCount == monsterValue:
                monsterAttributes = monsterLine.split(",")
                # Do the fight and pass in the monster
                doorMonster = monster.Monster(monsterAttributes[0],monsterAttributes[1],monsterAttributes[2],monsterAttributes[3],monsterAttributes[4],monsterAttributes[5])
                combatTextInterface(player,doorMonster,lootTable)
                break
            # Didn't find the monster we are looking for
            if lineCount == numOfMonsterLines:
                print("We reached the end of the monster file without finding the assigned monster. Something went wrong.")
                break
            # Increment to look at the next line
            lineCount += 1



def lootTheRoom(player,monster,lootTable): 
    lenOfLootTable = len(lootTable)
    for i in range(monster.getLootGain()):
        randomSelector = random.randint(0,lenOfLootTable)
        print("The hero looted: " + str(lootTable[randomSelector].getName()))
        player.setCardsInHand(lootTable[randomSelector])


def fight(player,monster):
    if player.getAttack() >= monster.getAttack():
        print("You won the battle! Loot the room.")
        lootTheRoom(player,monster)
    else:
        print("You can't fight the monster since you are weaker.")
        time.sleep(1)
        print("Either equip items to make yourself stronger, ask for assistance, or run.")


def run(player,monster):
    print("Running from the monster. Losing a level.")
    player.setLeve(player.getLevel() - 1)


def equipWeapon(player,weapon):
    player.setWeapon(weapon)


def equipItem(player,item):
    player.set(item)


def unequipWeapon(player,weapon):
    player.deleteWeapon(weapon)
# public imports
import time
import random

# private imports
import monster

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
        # TODO: We want to go to the main interactive interface
        # This is where I left off 



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
    player.set


def equipWeapon(player,weapon):
    player.setWeapon(weapon)


def equipItem(player,item):
    player.set(item)


def unequipWeapon(player,weapon):
    player.deleteWeapon(weapon)
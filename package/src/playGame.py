222992# This is the game Munchkins in a text-based format

# public imports
import time

# user defined imports
import initializeBackend as initialize
import createPlayers as createPlayers
import UserInterfaces.mainTextInterface as mainTextInterface


def main():
    # Introduce the game
    print("Welcome to Munchkins: Jacob Edition!")
    time.sleep(1)

    # Initialize our tables
    itemsTable, weaponsTable, monsterTable = initialize.initialize()

    # Capture the number of players
    numberOfPlayers = int(input("How many players would like to play? "))

    # Create all of the player objects
    arrayOfPlayers = createPlayers.playerCreation(numberOfPlayers, "", "")

    # Merge the itemsTable and weaponsTable for a loot table
    lootTable = weaponsTable + itemsTable

    # This is the flag for victory
    userResponse = False

    # Start the flow of the game
    # If the arrayOfPlayers is 1, we want to announce victory
    while len(arrayOfPlayers) != 1 and not userResponse:
        # We want to loop through the array of players and perform the typical turn actions for each one
        for playerArrayNum in range(len(arrayOfPlayers)):
            print("Starting turn for: " + arrayOfPlayers[playerArrayNum].getName())
            # Slow down the beginning of the turn
            time.sleep(1)

            # userResponse will be True if the current player is >= level 20, signifying a win
            userResponse = mainTextInterface.MainConsole(
                arrayOfPlayers[playerArrayNum], monsterTable, lootTable
            )

            if userResponse:
                break

            # Give time for the end of the turn
            time.sleep(1)

    print("Victory for " + str(arrayOfPlayers[0].getName()) + "!")


# Run the game
main()

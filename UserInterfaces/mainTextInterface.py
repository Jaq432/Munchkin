# The goal of this program is to be a driver for an interactive user input

import time

import moves
import UserInterfaces.developerTextInterface as developerTextInterface


def MainConsole(player,lootTable):
    nextPlayerTurn = False
    doorHasBeenKickedIn = False
    while nextPlayerTurn == False:
        print("What action would you like to take?")
        print("1. Kick in the door")
        print("2. List the cards in your hand")
        print("3. Equip an item from your hand")
        print("4. Sell items in your hand to gain a level")
        print("5. End your turn")
        print("6. Developer Interface")
        print("99. Exit the game")
        
        try:
            userChoice = int(input(""))
            print("")
        except:
            print("Invalid input. Please enter a number from the above list.")
            continue

        # Kick in the door
        if userChoice == 1 and doorHasBeenKickedIn == False:
            # Kick in the door
            # Looting the room also happens from that method
            doorHasBeenKickedIn = True
            moves.kickInDoor(player,lootTable)
            print("")
        
        elif userChoice == 1 and doorHasBeenKickedIn == True:
            print("This action has already been done this turn.")
            print("")
            time.sleep(1)

        # List cards in hand
        elif userChoice == 2:
            itemIndex = 1
            print("This is a list of the items in your hand:")
            for card in player.getCardsInHand():
                print(str(itemIndex) + ". " + str(card.getName()))
                itemIndex += 1
            print("")
            time.sleep(1)

        # Equip an item from hand
        elif userChoice == 3:
            print("3")

        # Sell items for levels
        elif userChoice == 4:
            print("4")

        elif userChoice == 5:
            if player.getLevel() >= 20:
                # This is the victory flag
                return True
            nextPlayerTurn = True

        elif userChoice == 6:
            print("Entering the Developer Interface.")
            declareVictory = developerTextInterface.MainConsole(player,lootTable)
            if declareVictory:
                return declareVictory
        
        elif userChoice == 99:
            print("Exiting the program.")
            exit()

        # Catch all
        else:
            print("That wasn't an option.")
            continue

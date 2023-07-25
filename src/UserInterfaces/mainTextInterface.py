# The goal of this program is to be a driver for an interactive user input

import time

import moves as moves
import UserInterfaces.developerTextInterface as developerTextInterface


def MainConsole(player, monsterTable, lootTable):
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
            moves.kickInDoor(player, monsterTable, lootTable)
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
            if player.getCardsInHand() != []:
                print("Which card would you like to equip?")
                cardIndex = 1
                for card in player.getCardsInHand():
                    print(str(cardIndex) + ". " + str(card.getName()))
                    cardIndex += 1
                print("")
                time.sleep(1)

                try:
                    cardChoice = int(input(""))
                    print("")
                except:
                    print("Invalid input. Please enter a number from the above list.")
                    print("")
                    time.sleep(1)
                    continue

                cardToEquip = player.getCardsInHand()[int(cardChoice) - 1]
                player.equipCard(cardToEquip)

            else:
                print("You don't have any cards in your hand.")
                print("")
                time.sleep(1)

        # Sell items for levels
        # This is quickly turning into madness
        elif userChoice == 4:

            # TODO
            # This is the plan: 
            # 1. Print off all available items/cards w/ values
            # 2. Take user input

            

            mergedItemList = []
            lengthOfEquippedItems = 0

            # Get our equipped cards
            for equippedWeapon in player.getWeapons():
                mergedItemList.append(equippedWeapon)
            for equippedItem in player.getItems():
                mergedItemList.append(equippedItem)
            
            # Get the list of equipped cards
            lengthOfEquippedItems = len(mergedItemList) + 1

            # Get the remaining cards in our hand
            for notEquippedCard in player.getCardsInHand():
                mergedItemList.append(notEquippedCard)
            
            # Make a list of indexes that we will be selling
            listOfCardIndexesToSell = []

            doneWithSellingCards = False
            while not doneWithSellingCards:
                # List out all of the cards that we are going to sell
                print("This is a list of the cards that you can sell:")
                index = 1
                for card in mergedItemList:
                    # If the card is equipped 
                    if index <= lengthOfEquippedItems:
                        print(str(index) + ": Equipped :" + str(card.getName()))
                    # If the card is in our hand
                    else:
                        print(str(index) + ": In Hand :" + str(card.getName()))
                    index += 1
                time.sleep(1)

                # Ask what card they want to sell 
                chosenCardIndex = input("Please select a number for the card that you want to sell: ")

                listOfCardIndexesToSell = []

                # Set the index back to 1 so we can get the right card
                itemIndex = 1

                # Make a location to hold the cards we are thinking about selling
                





        elif userChoice == 5:
            if player.getLevel() >= 20:
                # This is the victory flag
                return True
            nextPlayerTurn = True

        elif userChoice == 6:
            print("Entering the Developer Interface.")
            declareVictory = developerTextInterface.MainConsole(player, lootTable)
            if declareVictory:
                return declareVictory

        elif userChoice == 99:
            print("Exiting the program.")
            exit()

        # Catch all
        else:
            print("That wasn't an option.")
            continue

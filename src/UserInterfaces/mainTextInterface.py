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
        print("4. Sell items for gold")
        print("5. Exchange 1000g for a character level up.")
        print("6. End your turn")
        print("9. Developer Interface")
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
            if len(player.getCardsInHand()) == 0:
                print("You don't have any cards in your hand.")
                print("")
                time.sleep(1)

            else:
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
                print("This is a list of the cards that you can equip:")
                cardIndex = 1
                for card in player.getCardsInHand():
                    print(str(cardIndex) + ". " + str(card.getName()))
                    cardIndex += 1
                print("")
                time.sleep(1)
                userInput = input("What card would you like to equip? ")
                try:
                    userInputInt = int(userInput)
                    print("")
                    cardToEquip = player.getCardsInHand()[int(userInputInt) - 1]
                    player.equipCard(cardToEquip)
                except:
                    print("Invalid Input. Please try again.")
                    print("")
                    time.sleep(1)
            else:
                print("You don't have any cards in your hand.")
                print("")
                time.sleep(1)

        # Sell items for levels
        elif userChoice == 4:

            doneWithSellingCards = False
            while not doneWithSellingCards:

                mergedItemList = []
                lengthOfEquippedItems = 0

                # Get our equipped cards
                for equippedWeapon in player.getWeapons():
                    mergedItemList.append(equippedWeapon)
                for equippedItem in player.getItems():
                    mergedItemList.append(equippedItem)
                
                # Get the list of equipped cards
                lengthOfEquippedItems = len(mergedItemList)

                # Get the remaining cards in our hand
                for notEquippedCard in player.getCardsInHand():
                    mergedItemList.append(notEquippedCard)

                if len(mergedItemList) == 0:
                    print("You don't have any cards in your hand.")
                    print("")
                    time.sleep(1)
                    doneWithSellingCards = True
                    break

                # Show the user's gold quantity
                print("Your current gold: " + str(player.getGold()))
                # List out all of the cards that we are going to sell
                print("This is a list of the cards that you can sell:")
                index = 1
                for card in mergedItemList:
                    # If the card is equipped 
                    if index < lengthOfEquippedItems + 1:
                        print(str(index) + ": Equipped : " + str(card.getName()))
                    # If the card is in our hand
                    else:
                        print(str(index) + ": In Hand : " + str(card.getName()))
                    index += 1
                time.sleep(1)
                print("")

                # Ask what card they want to sell 
                print("Please type a number for the card that you want to sell.")
                print("Or you can type 'done' to exit this menu.")
                chosenCardIndex = input("What is your choice? ")

                # Flag that we are done with selling cards
                if str(chosenCardIndex).lower() == "done":
                    doneWithSellingCards = True
                    continue
                else:
                    # Catch bad inputs
                    try:
                        chosenCardIndexInt = int(chosenCardIndex) - 1
                    except:
                        print("Input invalid. Please try again.")
                        continue
                    
                    if chosenCardIndexInt >= len(mergedItemList):
                        print("Value entered was out of the range of listed cards. Please try again")
                        continue

                    for index, card in enumerate(mergedItemList):
                        if index == chosenCardIndexInt and lengthOfEquippedItems == 0:
                            player.sellHandCard(card)
                            break
                        if index == chosenCardIndexInt and index < lengthOfEquippedItems:
                            player.sellEquippedCard(card)
                            break
                        elif index == chosenCardIndexInt and index >= lengthOfEquippedItems:
                            player.sellHandCard(card)
                            break

                    # Set the index back to 1 so we can get the right card
                    itemIndex = 1

                    # Give some space for formatting
                    print("")

        elif userChoice == 5:
            print("Performing this action costs 1000g.")
            time.sleep(1)
            currentUserGold = int(player.getGold())
            if currentUserGold < 1000:
                print("")
                print("You don't have enough gold to make this action.")
                time.sleep(1)
                print("")
            else:
                userInput = input("Are you sure you want to continue? y/n ")
                if userInput.lower() == 'y':
                    currentPlayerLevel = int(player.getLevel())
                    updatedUserGold = currentUserGold - 1000
                    player.setLevel(currentPlayerLevel + 1)
                    print("Player level is now: " + str(player.getLevel()))
                    player.setGold(updatedUserGold)
                    print("Player gold total is now: " + str(player.getGold()))
                    
                elif userInput.lower() == 'n':
                    print("")
                else:
                    print("User input wasn't an option. Please try again.")
                
        elif userChoice == 6:
            if player.getLevel() >= 20:
                # This is the victory flag
                return True
            nextPlayerTurn = True

        elif userChoice == 9:
            print("Entering the Developer Interface.")
            declareVictory = developerTextInterface.MainConsole(player, lootTable)
            if declareVictory:
                return True

        elif userChoice == 99:
            print("Exiting the program.")
            exit()

        # Catch all
        else:
            print("That wasn't an option.")
            continue

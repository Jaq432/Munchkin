# The goal of this program is to be a driver for an interactive user input

import time

import moves as moves
import UserInterfaces.developerTextInterface as developerTextInterface


def MainConsole(player, monster, lootTable):
    nextPlayerTurn = False
    while nextPlayerTurn == False:
        print("What action would you like to take?")
        print(
            "Your current power is: "
            + str(player.getAttack())
            + " The monster's attack is: "
            + str(monster.getAttack())
        )
        print("1. Battle with your current power")
        print("2. List the cards in your hand")
        print("3. Equip an item from your hand")
        print("4. Sell items for gold")
        print("5. Exchange 1000g for a character level up.")
        print("6. Run and lose level(s) based on the monster.")
        print("9. Developer Interface")
        print("99. Exit the game")

        try:
            userChoice = int(input(""))
            print("")
        except:
            print("Invalid input. Please enter a number from the above list.")
            continue

        # Go to battle with the monster
        if userChoice == 1:
            for playerClass in player.getClass():
                if playerClass.getName() == "Archer":
                    pass
                    # TODO implement functionality that checks the type of the monster
                    # if it is a beast, archers get +3 attack against them. 
                    # This can be done by getting the player's attack once and checking the monster's type,
                    # then applying the offset
            if monster.getAttack() > player.getAttack():
                print("You don't have the strength to fight this monster.")
                time.sleep(1)
                print(
                    "Either equip items, ask for assistance from another player, or run from the fight."
                )
                print("")
            if player.getAttack() >= monster.getAttack():
                print("You have the strength to defeat this monster.")
                time.sleep(1)
                print("You can now loot the room.")
                moves.lootTheRoom(player, monster, lootTable)
                time.sleep(1)
                # Adjust the character's level
                player.setLevel(player.getLevel() + monster.getLevelsGain())
                print("Your character is now level " + str(player.getLevel()))
                return

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

        # Equip an card from hand
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
                for equippedClass in player.getClass():
                    mergedItemList.append(equippedClass)
                
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
                        print(str(index) + ": Equipped : " + str(card.getName()) + " : " + str(card.getCost()))
                    # If the card is in our hand
                    else:
                        print(str(index) + ": In Hand : " + str(card.getName()) + " : " + str(card.getCost()))
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
                            print("Selling equipped Card.")
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
                    player.setGold(updatedUserGold)
                    
                elif userInput.lower() == 'n':
                    print("")
                else:
                    print("User input wasn't an option. Please try again.")

        # Run from the fight and lose levels based on the monster
        elif userChoice == 6:
            # Adjust the character's level
            player.setLevel(player.getLevel() - monster.getLevelsGain())
            print("Your character is now level " + str(player.getLevel()))
            nextPlayerTurn = True

        elif userChoice == 9:
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

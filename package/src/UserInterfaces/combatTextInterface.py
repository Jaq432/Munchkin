# The goal of this program is to be a driver for an interactive user input

import time

import moves as moves
import UserInterfaces.developerTextInterface as developerTextInterface


def MainConsole(player, monster, lootTable):
    nextPlayerTurn = False
    doorHasBeenKickedIn = False
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
        print("4. Sell items in your hand to gain a level")
        print("5. Run")
        print("6. Return to the previous menu")
        print("7. Developer Interface")
        print("99. Exit the game")

        try:
            userChoice = int(input(""))
            print("")
        except:
            print("Invalid input. Please enter a number from the above list.")
            continue

        # Go to battle with the monster
        if userChoice == 1:
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
            itemIndex = 1
            print("This is a list of the cards in your hand:")
            if player.getCardsInHand() != None:
                for card in player.getCardsInHand():
                    print(str(itemIndex) + ". " + str(card.getName()))
                    itemIndex += 1
                print("")
                time.sleep(1)
            else:
                print("You don't have any cards in your hand.")
                print("")
                time.sleep(1)

        # Equip an card from hand
        elif userChoice == 3:
            if player.getCardsInHand() != None:
                print("Which card would you like to equip?")
                cardIndex = 1
                for card in player.getCardsInHand():
                    print(str(cardIndex) + ". " + str(card.getName()))
                    cardIndex += 1
                print("")
                time.sleep(1)
                cardChoice = input("Please enter the card number: ")
                cardIndex = 1
                for card in player.getCardsInHand():
                    if cardIndex == cardChoice:
                        player.equipCard(card)
            else:
                print("You don't have any cards in your hand.")
                print("")
                time.sleep(1)

        # Sell items for levels
        elif userChoice == 4:
            print("4")

        elif userChoice == 5:
            print("5")

        elif userChoice == 6:
            if player.getLevel() >= 20:
                # This is the victory flag
                return True
            nextPlayerTurn = True

        elif userChoice == 7:
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

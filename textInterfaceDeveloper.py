# The goal of this program is to be a driver for an interactive user input

import time

import moves


def MainConsole(player,lootTable):
    returnToPlayerInterface = False
    while returnToPlayerInterface == False:
        print("What would you like to check?")
        print("1. Player Name")
        print("2. Player Cards in Hand")
        print("3. Player Race")
        print("4. Player Class")
        print("5. Player Weapons")
        print("6. Player Weapons Count")
        print("7. Player Attack")
        print("8. Player Level")
        print("98. Declare victory for this character.")
        print("99. Return to the player interface.")
        
        try:
            userChoice = int(input(""))
            print("")
        except:
            print("Invalid input. Please enter a number from the above list.")
            continue

        # Player Name
        if userChoice == 1:
            print("This is your name:")
            print(player.getName())

        # List cards in hand
        elif userChoice == 2:
            itemIndex = 1
            print("This is a list of the items in your hand:")
            for card in player.getCardsInHand():
                print(str(itemIndex) + ". " + str(card.getName()))
                itemIndex += 1
            print("")
            time.sleep(1)

        # Player Race
        elif userChoice == 3:
            print("This is your race:")
            print(player.getRace())

        # Player Class
        elif userChoice == 4:
            print("This is your class:")
            print(player.getClass())

        # Player Weapons
        elif userChoice == 5:
            itemIndex = 1
            print("This is a list of your equipped weapons:")
            for weapon in player.getWeapons():
                print(str(itemIndex) + ". " + str(card.getName()))
                itemIndex += 1

        # Player Weapons Count
        elif userChoice == 6:
            print("This is how many weapons you have equipped:")
            print(player.getWeaponCount())

        # Player Attack
        elif userChoice == 7:
            print("This is your character's attack:")
            print(player.getAttack())

        # Player Level
        elif userChoice == 8:
            print("This is your character's level:")
            print(player.getLevel())

        # Declare Victory
        elif userChoice == 98:
            print("Declaring victory.")
            return True

        # Return to the player interface
        elif userChoice == 99:
            print("Returning to the player interface.")
            returnToPlayerInterface = True

        # Catch all
        else:
            print("That wasn't an option.")
            continue

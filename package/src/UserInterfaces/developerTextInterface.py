# The goal of this program is to be a driver for an interactive user input

import time

import moves
import Types.item as item
import Types.weapon as weapon
import Types.monster as monster


def MainConsole(player, lootTable):
    returnToPlayerInterface = False
    while returnToPlayerInterface == False:
        print("What would you like to check?")
        print("1. Report Player Name")
        print("2. Report Player Cards in Hand")
        print("3. Report Player Race")
        print("4. Report Player Class")
        print("5. Report Player Weapons")
        print("6. Report Player Items")
        print("7. Report Player Attack")
        print("8. Report Player Level")
        print("9. Give player test cards")
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
            for equippedWeapon in player.getWeapons():
                print(str(itemIndex) + ". " + str(equippedWeapon.getName()))
                itemIndex += 1

        # Player Items
        elif userChoice == 6:
            itemIndex = 1
            print("This is a list of your equipped items:")
            for equippedItem in player.getItems():
                print(str(itemIndex) + ". " + str(equippedItem.getName()))
                itemIndex += 1

        # Player Attack
        elif userChoice == 7:
            print("This is your character's attack:")
            print(player.getAttack())

        # Player Level
        elif userChoice == 8:
            print("This is your character's level:")
            print(player.getLevel())

        # Equip Test Cards
        elif userChoice == 9:
            print("Equipping a predetermined set of cards.")
            card1 = item.Item("Basic Helmet","head",1,50,"Better than nothing (leather)")
            card2 = item.Item("Basic Chest","chest",1,50,"Better than nothing (leather)")
            card3 = item.Item("Basic Gloves","hands",1,50,"Better than nothing (leather)")
            card4 = item.Item("Basic Boots","feet",1,50,"Better than nothing (leather)")
            card5 = weapon.Weapon("Iron Claymore","2 hand",2,200,"Clunky but effective")
            player.equipCard(card1)
            player.equipCard(card2)
            player.equipCard(card3)
            player.equipCard(card4)
            player.equipCard(card5)

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

        print("")

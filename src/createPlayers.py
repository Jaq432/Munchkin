import Types.player as player


def playerCreation(numberOfPlayers, testPlayer1, testPlayer2):
    # Make an array which holds all of the generic player info to return
    arrayOfPlayers = []

    if testPlayer1 == "" and testPlayer2 == "":
        for _ in range(numberOfPlayers):
            # This will need to be updated so we can create players using player.py
            playerName = input("What is the name of this player? ")

            # Start creating the player array
            newPlayer = player.Player(
                playerName, #  Name
                1,  #  Level
                [], #  Race
                [], #  Class
                [], #  Weapons
                [], #  Items
                1,  #  Attack
                [], #  Cards in hand
                0,  #  Personal Gold
            )
            arrayOfPlayers.append(newPlayer)
        # Spacing for interface
        print("")

    # Return the player array for use in the game
    return arrayOfPlayers

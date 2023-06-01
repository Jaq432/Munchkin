import Types.player as player

def createPlayers(numberOfPlayers):
    # Make an array which holds all of the generic player info to return
    arrayOfPlayers = []

    for playerNum in range(numberOfPlayers):
        # This will need to be updated so we can create players using player.py
        playerName = input("What is the name of this player? ")
        
        # Start creating the player array
        arrayOfPlayers.append(player.Player(playerName))
    
    # Return the player array for use in the game
    return arrayOfPlayers
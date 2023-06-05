import Types.player as player

def createPlayers(numberOfPlayers, testPlayer1, testPlayer2):
    # Make an array which holds all of the generic player info to return
    arrayOfPlayers = []

    if testPlayer1 == "" and testPlayer2 == "":
        for playerNum in range(numberOfPlayers):
            # This will need to be updated so we can create players using player.py
            playerName = input("What is the name of this player? ")
            
            # Start creating the player array
            arrayOfPlayers.append(player.Player(playerName))
    # Used for testing
    else:
        arrayOfPlayers.append(player.Player(testPlayer1))
        arrayOfPlayers.append(player.Player(testPlayer2))
    
    # Return the player array for use in the game
    return arrayOfPlayers

def test_createPlayers():
    assert createPlayers(2,"a","b")
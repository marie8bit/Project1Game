
#main funtion calls file reader and asks for user name
from FileWorker import FileWorker
from Player import Player
from Game import Game
#handles error if file is not found
def main():
    playerList = []
    filePlayerList = FileWorker.readFile()
    for player in filePlayerList:
        playerList.append(player)



    #get user name to change win value or create a new player
    print ("Enter your name")
    #get input from user

    newName = input()
    #validates user input
    while (newName == ''):
        print ('Please enter your name')
        newName=input()

    newPlayer = getPlayer(newName, playerList)

    game = Game(newPlayer, playerList)
    game.go()


#handles file not found ramifications in FileWorker function call
def getPlayer(newName, playerList):
    gplayer = Player(newName, 0)

    #identifies if user exists or if a new player should be created
    for player in playerList:
        #looks for user in list to alter win value for player
        #initializes game with existing user
        if (player.name == gplayer.name):
            playerList.remove(player)
            gplayer = player
    return gplayer

    #creates playerList if not created with FileWorker function
if __name__ == '__main__':
    main()
# except NameError as ne:
#     playerList =[]
#     #starts game with new user
#     plyr= Player(newName, 0)
#     game = Game(plyr, playerList)
#     game.go()


#main funtion calls file reader and asks for user name
from FileWorker import FileWorker
from Player import Player
from Game import Game
#handles error if file is not found
try:
    playerList=FileWorker.readFile()
except UnboundLocalError as ule:
    print('File not found')
except IOError as err:
    print ('File not found')
#get user name to change win value or create a new player
print ("Enter your name")
#get input from user

newName = input()
#validates user input
while (newName == ''):
    print ('Please enter your name')
    newName=input()
#handles file not found ramifications in FileWorker function call
try:
    #identifies if user exists or if a new player should be created
    for player in playerList:
        #looks for user in list to alter win value for player
        #initializes game with existing user
        if (player.name == newName):
            playerList.remove(player)
            Game(player, playerList)
    #create new user
    plr=Player(newName, 0)
    #initialize game for new user
    Game(plr, playerList)
#creates playerList if not created with FileWorker function
except NameError as ne:
    playerList =[]
    #starts game with new user
    plyr= Player(newName, 0)
    game = Game(plyr, playerList)
    game.go()

from FileWorker import FileWorker
from Player import Player
from Game import Game

playerList=FileWorker.readFile()
print ("Enter your name")
#get input from user
newName = input()
#Player.name+'|'+Player.wins.toString()

while True:

    for player in playerList:
        print(player.name)
        if (player.name == newName):
            playerList.remove(player)
            Game(player, playerList)
    plr=Player(newName, 0)
    Game(plr, playerList)

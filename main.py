from FileWorker import FileWorker
from Player import Player
from Game import Game

playerList=FileWorker.readFile()
print ("Enter your name")
#get input from user
newName = input()
#Player.name+'|'+Player.wins.toString()

for player in playerList:
    if (player.name == newName) in playerList:
        Game(Player, playerList)
    else:
        plr=Player(newName, 0)
        playerList.append(plr)
        Game(plr, playerList)

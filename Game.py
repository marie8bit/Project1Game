import random
from Player import Player
from FileWorker import FileWorker
class Game:

    def __init__(self, player, playerList):
        comp = Player('Computer', 0)
        Game.playAgain(player, playerList)


    def tryAgain(player, playerList) :
        print('Enter a number to play')
        print('1:Rock')
        print('2:Paper')
        print('3:Scissors')
        # TODO: daa validation needed
        throw = int(input())

        compT = Game.compThrow()
        Game.winning(throw, compT, player, playerList)
    def playAgain(player, playerList):
        print('Would you like to play again? Enter y for Yes')
        again = input().lower()

        if (again == 'y'):
            Game.tryAgain(player, playerList)
        else:
            playerList.append(player)
            FileWorker.writeFile(playerList)

    def compThrow():

        #generate a random number
        compNum = random.randint(1,3)
        print(str(compNum))
        return compNum

    def winning(plr, puter, ob, playerList):

        if plr != puter:
            if (1 in [plr, puter] and 2 in [plr, puter]):

                if (plr == 2):
                    ob.win()
                else:
                    print ('Computer wins')


            elif (2 in [plr, puter] and 3 in [plr, puter]):

                if (plr == 3):
                    ob.win()
                else:
                    print ('Computer wins')


            elif (1 in [plr, puter] and 3 in [plr, puter]):

                if (plr == 1):
                    ob.win()
                else:
                    print ('Computer wins')
            Game.playAgain(ob, playerList)


        else:
            print ('Tie, try again')
            Game.tryAgain(ob, playerList)

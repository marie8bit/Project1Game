import random
from Player import Player
from FileWorker import FileWorker
class Game:

    def __init__(self, player, playerList):
        tie = False
        quit = False
        comp = Player('Computer', 0)
        self.player = player
        while quit == False:
            print('Would you like to play again? Enter y for Yes')
            again = input().lower()

            if (again == 'y'):

                tie = True
            else:
                quit = True
            while tie == True:
                print('Enter a number to play')
                print('1:Rock')
                print('2:Paper')
                print('3:Scissors')
                # TODO: daa validation needed
                throw = int(input())

                compT = Game.compThrow()
                Game.winning(throw, compT, player)
        FileWorker.writeFile(playerList)

    def compThrow():

        #generate a random number
        compNum = random.randint(1,3)
        print(str(compNum))
        return compNum

    def winning(plr, puter, ob):

        if plr != puter:
            Game.tie = False
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


        else:
            print ('Tie, try again')
            #tie = True

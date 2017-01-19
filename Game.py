import random
from Player import Player
from FileWorker import FileWorker
#class to handle game functions
class Game:

    def __init__(self, player, playerList):
        #comp = Player('Computer', 0)
        Game.playAgain(player, playerList)

    #provide game options to user
    def tryAgain(player, playerList) :
        print('Enter a number to play')
        print('1:Rock')
        print('2:Paper')
        print('3:Scissors')
        #validate user input
        try:
            throw = int(input())
        except ValueError:
            print('Your entry must be a number from the list')
            tryAgain(player, playerList)
        compT = Game.compThrow()
        #process user input
        if (throw == ''):
            print('Please select a number from the list')
        #handles valid input
        elif (throw in [1,2,3]):
            Game.winning(throw, compT, player, playerList)
        #handles int input not in selection options
        else:
            print('Please select a number from the list')

    #allows user to end the program
    def playAgain(player, playerList):
        print('Would you like to play? Enter y for Yes')
        again = input().lower()

        if (again == 'y'):
            Game.tryAgain(player, playerList)
        else:
            playerList.append(player)
            FileWorker.writeFile(playerList)
    #gets comp play
    def compThrow():

        #generate a random number
        compNum = random.randint(1,3)
        #display computer selection
        print(str(compNum))
        return compNum
    #function to handle user information about who wins a game
    def winning(plr, puter, ob, playerList):

        if plr != puter:
            if (1 in [plr, puter] and 2 in [plr, puter]):

                if (plr == 2):
                    #call player class function for adjusting a players wins attribute
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
            #asks user if they want to play again
            Game.playAgain(ob, playerList)

        #makes a player play again to settle a tie
        else:
            print ('Tie, try again')
            Game.tryAgain(ob, playerList)

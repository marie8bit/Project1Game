import random
from Player import Player
from FileWorker import FileWorker
#class to handle game functions
class Game:

    def __init__(self, player, playerList):
        self.playerList = playerList
        self.player = player

    def go(self):
        #comp = Player('Computer', 0)
        self.playAgain( )


    #provide game options to user
    def tryAgain(self) :
        print('Enter a number to play')
        print('1:Rock')
        print('2:Paper')
        print('3:Scissors')
        #validate user input
        try:
            throw = int(input())
        except ValueError:
            print('Your entry must be a number from the list')
            self.tryAgain()
        compT = self.compThrow()
        #process user input
        if (throw == ''):
            print('Please select a number from the list')
        #handles valid input
        elif (throw in [1,2,3]):
            there_was_a_winner = self.winning(throw, compT)
            if there_was_a_winner:
                self.playAgain()
            else:
                self.tryAgain()
        #handles int input not in selection options
        else:
            print('Please select a number from the list')

    #allows user to end the program
    def playAgain(self):
        print('Would you like to play? Enter y for Yes')
        again = input().lower()

        if (again == 'y'):
            self.tryAgain()
        else:
            self.playerList.append(self.player)
            FileWorker.writeFile(self.playerList)

    #gets comp play
    def compThrow(self):

        #generate a random number
        compNum = random.randint(1,3)
        #display computer selection
        print(str(compNum))
        return compNum

    #function to handle user information about who wins a game
    def winning(self, player_throw, puter):

        if player_throw != puter:
            if (1 in [player_throw, puter] and 2 in [player_throw, puter]):

                if (player_throw == 2):
                    #call player class function for adjusting a players wins attribute
                    self.player.win()
                else:
                    print ('Computer wins')


            elif (2 in [player_throw, puter] and 3 in [player_throw, puter]):

                if (player_throw == 3):
                    self.player.win()
                else:
                    print ('Computer wins')


            elif (1 in [player_throw, puter] and 3 in [player_throw, puter]):

                if (player_throw == 1):
                    self.player.win()
                else:
                    print ('Computer wins')
            #asks user if they want to play again

            #self.playAgain()
            return True # indicate someone won

        #makes a player play again to settle a tie
        else:
            print ('Tie, try again')
            #self.tryAgain()
            return False   #  no winner

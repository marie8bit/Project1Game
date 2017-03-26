import random
from Player import Player
from FileWorker import FileWorker
#class to handle game functions
class Game:

    def __init__(self, player, playerList):
        self.playerList = playerList
        self.player = Player(player.name, player.wins)


    def go(self):
        #comp = Player('Computer', 0)
        throw = self.tryAgain( )
        int_throw = self.validate_input_int(throw)
        pl_throw = self.validate_input_list(int_throw)
        compT = self.compThrow()
        there_was_a_winner, string = self.winning(pl_throw, compT)
        print (string)
        if there_was_a_winner:
            self.playAgain()
        else:
            self.go()

    #provide game options to user
    def tryAgain(self) :
        print('Enter a number to play')
        print('1:Rock')
        print('2:Paper')
        print('3:Scissors')
        throw = input()
        return throw

    def validate_input_int(self, throw):

        #validate user input
        try:
            pthrow = int(throw)
        except ValueError:
            print('Your entry must be a number')
            throw = input()
            pthrow = self.validate_input_int(throw)
        return pthrow

    def validate_input_list(self, pthrow):
        if (pthrow==1 or pthrow ==2 or pthrow == 3):
            return pthrow
        else:
            print('Your entry must be a number in the list')
            plathrow = self.validate_input_int(input())
            plthrow = self.validate_input_list(plathrow)
            return plthrow


    #allows user to end the program
    def playAgain(self):
        print('Would you like to play? Enter y for Yes')
        again = input().lower()

        if (again == 'y'):
            self.go()
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
                    string = self.player.win()

                else:
                    string = 'Computer wins'


            elif (2 in [player_throw, puter] and 3 in [player_throw, puter]):

                if (player_throw == 3):
                    string = self.player.win()

                else:
                    string= 'Computer wins'



            elif (1 in [player_throw, puter] and 3 in [player_throw, puter]):

                if (player_throw == 1):
                    string =self.player.win()

                else:
                    string =  'Computer wins'
            #asks user if they want to play again

            #self.playAgain()
            return True, string # indicate someone won

        #makes a player play again to settle a tie
        else:
            string = 'Tie, try again'
            #self.tryAgain()
            return False, string   #  no winner

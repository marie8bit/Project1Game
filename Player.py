#class to handle player attributes and functions
class Player:
    #initializes instance of Player
    def __init__(self, name, wins):
        self.name = name
        self.wins = wins
    #function to adjust Player wins attribute
    def win(self):
        self.wins+=1
        return str(self)
    #function to define how a Player instance is displayed to user
    def __str__(self):
        message = self.name + ' has won '+str(self.wins)+(' game!' if (self.wins == 1) else ' games!')
        return message

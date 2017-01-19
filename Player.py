class Player:
    def __init__(self, name, wins):
        self.name = name
        self.wins = wins

    def win(self):
        self.wins+=1
        print (self)

    def __str__(self):
        message = self.name + ' has won '+str(self.wins)+(' game!' if (self.wins == 1) else ' games!')
        return message

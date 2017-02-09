from Player import Player
import sys
#class for reading and writing to txt file
class FileWorker:

    def readFile():
        #try to handle file not found error
        try:
            #open file to read data
            f=open('records','r')
        #returns to function call
        except IOError as err:
            print ('File not found')

        list=[]
        #reads lines from file and adds Players to list
        for line in f:
            #line=line.strip(' '+'\n')
            ob = line.split('|')
            name = ob[0]
            #print (name)
            wins = int(ob[1])
            #print (wins)
            pl = Player(name, wins)
            list.append(pl)
        for player in list:
            print(str(player))
        #returns list of players to main function call
        return list
        #close resource
        f.close()
    #writes list to txt file and closes the program
    def writeFile(list):
        #sort list to display highest scores first
        list=sorted(list, key=lambda Player: Player.wins, reverse=True)
        #clears file of data
        open('records', 'w').close()
        #opens file to write data
        w=open('records', 'w')
        for Player in list:
            #shows final results to user
            print(str(Player))
            #formats data for writing to file
            name = Player.name
            wins= str(Player.wins)
            w.write(name+'|'+wins+'\n')
        #close resource
        w.close()
        #let user know program is closed
        print('Goodbye')
        #end program
        ##sys.exit()

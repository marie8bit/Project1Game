from Player import Player
import sys
class FileWorker:

    def readFile():
        f=open('records','r')

        list=[]
        for line in f:
            #line=line.strip(' '+'\n')
            ob = line.split('|')
            # TODO: needs exception handling
            name = ob[0]
            print (name)
            wins = int(ob[1])
            print (wins)
            pl = Player(name, wins)
            list.append(pl)
        print([str(Player) for Player in list])

        return list
        f.close()

    def writeFile(list):
        list=sorted(list, key=lambda Player: Player.wins, reverse=True)
        open('records', 'w').close()
        w=open('records', 'w')
        for Player in list:
            name = Player.name
            print (name)
            wins= str(Player.wins)
            print (wins)
            w.write(name+'|'+wins+'\n')
        w.close()
        print('Goodbye')
        sys.exit()

f=open('records','r')

list=[]
for line in f:
    line=line.strip(' '+'\n')
    list.append(line.split('|'))

list.append(['Claire','4'])
print(list)
f.close()
open('records', 'w').close()
w=open('records', 'w')
for elem in list:
    name = elem[0]
    print (name)
    wins=elem[1]
    print (wins)
    w.write(name+'|'+wins+'\n')
w.close()

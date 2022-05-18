fo = open('C:/Users/17RPakulski.ACC/revistionfile.txt','r')

fw = open('filewritee.txt', 'w')
fwr = open('filewritee.txt', 'r')

caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

countcaps = 0
countspaces = 0
countnumbers = 0
countwords = 0

for line in fo:
    countspaces += line.count(' ')
    for item in line.split():
        countwords += 1
        for ch in item:
            if ch in caps:
                countcaps += 1
            if ch in numbers:
                countnumbers += 1
    
fw.write('Capitals = ' + str(countcaps))
fw.write('\nSpaces = ' + str(countspaces))
fw.write('\nWords = ' + str(countwords))
fw.write('\nNumbers = ' + str(countnumbers))




fw.close()

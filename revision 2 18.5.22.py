fo = open('C:/Users/17RPakulski.ACC/revisionfileaverage.txt', 'r')

listmedian = []
lenghtoflist = 0

addAll = 0
allAmount = 0

for line in fo:
    for item in line.split(','):
        listmedian.append(item)
        allAmount += 1
        addAll += float(item)
        



mean = addAll / allAmount

mean = round(mean,2)
#print('mean = ' + str(mean))


lenghtoflist = len(listmedian)




print('mean = ' + str(mean))
if lenghtoflist % 2:
    halfoflist = int(lenghtoflist / 2)
    print('median = ' + listmedian[halfoflist])

    








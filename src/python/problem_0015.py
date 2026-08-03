column = 20

listDict = {
    0 : 1,
    1 : [i for i in range(column + 1, 0, -1)]
}

def newColumn(index):
    copyList = list(listDict[index])
    tempList = []
    for i in range(column+1):
        tempList.append(sum(copyList))
        copyList.pop(0)
    return tempList
    
for i in range(2,column):
    newList = newColumn(i-1)
    listDict[i] = newList
print((listDict[len(listDict)-1][0])*2)
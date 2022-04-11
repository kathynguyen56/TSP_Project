#def getPathDistance(path,cityMap):
def getPathDistance(currentPath, cityMap):
    distance = 0;
    for index in range((len(currentPath)-1)):
        nextDistance = cityMap[currentPath[index]][currentPath[(index + 1)]]
        #print(nextDistance)
        distance = distance + nextDistance

    nextDistance = cityMap[currentPath[(len(currentPath) -1)]][currentPath[0]]
    #print(nextDistance)
    distance = distance + nextDistance
    return distance

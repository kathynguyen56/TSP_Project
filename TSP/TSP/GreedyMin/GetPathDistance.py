
def getPathDistance(path,cityMap):

    distance = 0;
    for pathIndex in range((len(path)-1)):

        nextDistance = cityMap[path[pathIndex]][path[(pathIndex + 1)]]
        distance = distance + nextDistance

    nextDistance = cityMap[path[(len(path) -1)]][path[0]]

    distance = distance + nextDistance

    return distance

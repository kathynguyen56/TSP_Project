
def getPathDistance(path,cityMap):
    #print("Get path distance.")
    #print(cityMap)
    distance = 0;
    for pathIndex in range((len(path)-1)):
        #print("path Index", pathIndex)
        #print("From City", path[pathIndex])
        #print("To City", path[(pathIndex + 1)])
        nextDistance = cityMap[path[pathIndex]][path[(pathIndex + 1)]]
        #print(nextDistance)
        distance = distance + nextDistance
        #print("Distance so far:", distance)

    #nextDistance = cityMap[path[(len(path) -1)]][path[0]]
    #print("path Index", len(path))
    #print("From City", path[(len(path)-1)])
    #print("To City", path[0])
    #print(nextDistance)
    #distance = distance + nextDistance
    #print("total path distance", distance)
    return distance

from GetPath import getRandomPath
from GetPathDistance import getPathDistance
import time
import csv

def guessAndCheck(path,cityMap, cityCount):
    print("Start of guess-and-check algorithm.")
    
    startTime = time.time()
    failToImprove = 0
    tempPath = [0 for i in range(len(path))]
    
    getRandomPath(tempPath)
    shortestDistance = getPathDistance(tempPath,cityMap)
    print("Shortest distance:",shortestDistance)
    
    with open('g&c-mpi.csv','w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Guess and Check', cityCount])
        writer.writerow(['New Shortest Path', 'Time'])
        writer.writerow([shortestDistance, '-'])
        
    path = tempPath.copy()
    
    #tempDistance = 0
#with pymp.Parallel(2) as p:
    for failToImprove in range(0, 1000000):
    
        getRandomPath(tempPath)
        tempDistance =  getPathDistance(tempPath,cityMap)
        
        if(tempDistance < shortestDistance):
            path = tempPath.copy()
            shortestDistance = tempDistance
            stopTime = time.time()
            print("New shortest G&C distance and time:", shortestDistance, (stopTime - startTime))
            with open('g&c-mpi.csv','a') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([shortestDistance, stopTime - startTime])
            
        else:
            failToImprove = failToImprove + 1

    stopTime = time.time()
    print("Guess and Check Path:", path)
    distance = getPathDistance(path, cityMap)
    print("Guess and Check distance and time:", distance, (stopTime - startTime))
    
    
   
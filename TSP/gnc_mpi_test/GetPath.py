import random
import numpy as np

def getRandomPath(path):
    
    citiesToVisit = [0 for i in range(len(path))]
    
    for index in range(len(path)):
        citiesToVisit[index] = index
        
    path[0] = random.choice(citiesToVisit)
    citiesToVisit.remove(path[0])
    
    for pathIndex in range(1,len(path)):
        nextCity = random.choice(citiesToVisit)
        path[pathIndex] = nextCity
        citiesToVisit.remove(path[pathIndex])

    

import numpy as np
import random
import time
from GetPathDistance import getPathDistance

def twoSwap(path, distance, cityMap):
    twoSwapCount = 0
    
    #print("\n", cityMap)
    print("\nCurrent path:", path)
    print("Distance:", distance)
    print("\nChecking for two-swaps.")
    
    for i in range(1, (len(path) - 2)):
        cityA = i
        cityB = i + 1
        
        #print("\nShould we swap", cityA, "and", cityB, "?")
        #print ("Path [A]:", path[cityA], "Path [B]:", path[cityB])
        
        distAB = cityMap[path[cityA - 1]][path[cityA]] + cityMap[path[cityA]][path[cityB]] + cityMap[path[cityB]][path[cityB + 1]]
        #print("Distance from", path[cityA - 1], "-", path[cityA], "-", path[cityB], "-", path[cityB + 1], ":", distAB)
        
        distBA = cityMap[path[cityA - 1]][path[cityB]] + cityMap[path[cityB]][path[cityA]] + cityMap[path[cityA]][path[cityB + 1]]
        #print("Distance from", path[cityA - 1], "-", path[cityB], "-", path[cityA], "-", path[cityB + 1], ":", distBA)
        
        if (distBA < distAB):
            #print("Swapping")
            
            tempVal = path[cityA]
            path[cityA] = path[cityB]
            path[cityB] = tempVal
            
            distance = getPathDistance(path, cityMap)
            #print("New distance:", distance)
            
            twoSwapCount += 1
            
        #else:
            #print("No swap.")

    return twoSwapCount
    
def threeSwap(path, distance, cityMap):
    threeSwapCount = 0
    print("\nChecking for three-swaps.")
    
    for i in range(0, (len(path) - 5)):
        cityA = i
        cityB = i + 1
        cityC = i + 2
        cityD = i + 3
        cityE = i + 4
        swap = False
        newMin = distance
        
        #print("Should we swap?")
    
        distABCDE = cityMap[path[cityA]][path[cityB]] + cityMap[path[cityB]][path[cityC]] + cityMap[path[cityC]][path[cityD]] + cityMap[path[cityD]][path[cityE]]
        #print("Distance", path[cityA], "-", path[cityB], "-", path[cityC], "-", path[cityD], "-", path[cityE], ":", distABCDE)
        
        distABDCE = cityMap[path[cityA]][path[cityB]] + cityMap[path[cityB]][path[cityD]] + cityMap[path[cityD]][path[cityC]] + cityMap[path[cityC]][path[cityE]]
        #print("Distance", path[cityA], "-", path[cityB], "-", path[cityD], "-", path[cityC], "-", path[cityE], ":", distABDCE)
        if (distABDCE < distABCDE):
            #print("Swapping")
            tempVal = path[cityC]
            path[cityC] = path[cityD]
            path[cityD] = tempVal
            threeSwapCount += 1
        
        distACBDE = cityMap[path[cityA]][path[cityC]] + cityMap[path[cityC]][path[cityB]] + cityMap[path[cityB]][path[cityD]] + cityMap[path[cityD]][path[cityE]]
        #print("Distance", path[cityA], "-", path[cityC], "-", path[cityB], "-", path[cityD], "-", path[cityE], ":", distACBDE)
        if (distACBDE < distABCDE):
            #print("Swapping")
            tempVal = path[cityB]
            path[cityB] = path[cityC]
            path[cityC] = tempVal
            threeSwapCount += 1
        
        distACDBE = cityMap[path[cityA]][path[cityC]] + cityMap[path[cityC]][path[cityD]] + cityMap[path[cityD]][path[cityB]] + cityMap[path[cityB]][path[cityE]]
        #print("Distance", path[cityA], "-", path[cityC], "-", path[cityD], "-", path[cityB], "-", path[cityE], ":", distACDBE)
        if (distACDBE < distABCDE):
            #print("Swapping")
            tempVal = path[cityB]
            path[cityB] = path[cityC]
            path[cityC] = path[cityD]
            path[cityD] = tempVal
            threeSwapCount += 1
            
        
        distADBCE = cityMap[path[cityA]][path[cityD]] + cityMap[path[cityD]][path[cityB]] + cityMap[path[cityB]][path[cityC]] + cityMap[path[cityC]][path[cityE]]
        #print("Distance", path[cityA], "-", path[cityD], "-", path[cityB], "-", path[cityC], "-", path[cityE], ":", distADBCE)
        if (distADBCE < distABCDE):
            #print("Swapping")
            tempVal = path[cityD]
            path[cityD] = path[cityC]
            path[cityC] = path[cityB]
            path[cityB] = tempVal
            threeSwapCount += 1
            
        
        distADCBE = cityMap[path[cityA]][path[cityD]] + cityMap[path[cityD]][path[cityC]] + cityMap[path[cityC]][path[cityB]] + cityMap[path[cityB]][path[cityE]]
        #print("Distance", path[cityA], "-", path[cityD], "-", path[cityC], "-", path[cityB], "-", path[cityE], ":", distADCBE)
        if (distADCBE < distABCDE):
            #print("Swapping")
            tempVal = path[cityB]
            path[cityB] = path[cityD]
            path[cityD] = tempVal
            threeSwapCount += 1
            
    return threeSwapCount      
            
        
        
        
        
        
        
    
    
    
    
    
    
    
        
        
    
    
            
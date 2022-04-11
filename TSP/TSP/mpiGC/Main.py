from array import array
#from Greedy import greedy

from GuessAndCheck import guessAndCheck
from LoadMap import loadMap

print("Welcome to Arianna's Shortest Path program. \nWorking through Guess-and-Check.")

cityCount = 10
print("Our city count is", cityCount)
path = [0 for i in range(cityCount)]

cityMap = loadMap(cityCount)

#filename = "g&c-mpi.csv"


    
guessAndCheck(path, cityMap, cityCount)
#greedy(path, cityMap)

#with open('g&c-mpi.csv','w') as csvfile:
                #writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                #writer.writerow([shortestDistance, stopTime - startTime])
                
#with open('g&c-mpi.csv','w') as csvfile:
        #writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #writer.writerow(['New Shortest Path', 'Time'])
        #writer.writerow([shortestDistance, '-'])

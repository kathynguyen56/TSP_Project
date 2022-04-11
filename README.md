# TSP_Project
For Software Engineering group project and OK High Perfomance Computing Competition.

Created serial and parallized code to solve the Shortest Path Problem using two different numpy functions (amax and argmin) that can be run on a raspberry pi4 cluster.
The algorithm used to find the shortest path is a greedy algorithm. With the greedy algorithm, the next city chosen for the path will be based on the city that has the shortest
distance value. Once a path has been found, it will calculate the overall distance. 

In order to run the parallized code on the cluster: 
 1. Need to get to the cloud directory, then into TSP (where the program is located), then finally into the folder the program is actually in. Ex: cloud/TSP/GreedyMinMPI
 2. Run the following command: mpiexec -hostfile /home/pi/hostfile -np **32** python3 /cloud/TSP/GreedyMinMPI/Main.py. This will run the code using 32 processors. To use
    a different number of processers simply change the number that has been bolded above. 

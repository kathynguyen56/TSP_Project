import sys
import os.path
from os import path
import numpy as np
import math


myArray = []
file = 'm0016x0016.bin'


myArray = np.fromfile(file, dtype=float)
print('numbers read in: ', len(myArray))
my2dArray = np.reshape(myArray,(int(math.sqrt(len(myArray))),int(math.sqrt(len(myArray)))),order='C')
print('shape of 2d array: ', my2dArray.shape)


print(my2dArray)

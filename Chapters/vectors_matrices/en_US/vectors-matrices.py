#import the python module that supports matrices
import numpy as np

# create an array
a = np.array([[5, 1, 3, -2], 
              [1, -1, 8, 4], 
              [6, 2, 1, 3]])

# create a vector 
b = np.array([1, 2, 3, -8])

#calculate the dot product
print(a.dot(b))
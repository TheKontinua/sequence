// import the python module that supports matrices
import numpy as np
// Use the function np.array to define a matrix that 
// contains specific values that you supply.
A = np.array([[5, 1, 3], 
              [1, -1, 8], 
              [6, 2, 1]])
// The transpose function returns 
A.transpose()

// create a matrix, B
B = np.array([[5, 1, 6], 
              [1, -1, 2], 
              [6, 2, 1]])
B.transpose()

// create a matrix, B
J = np.array([[5, 1, 3, 0], 
              [1, -1, 8, 11], 
              [6, 2, 1, -7]])
J.transpose()

// create an 8 by 10 Zero matrix.
 C = np.zeros((8, 10))
 C
 
// create an 8 by 8 Identity matrix 
 D = np.eye(8)
 D
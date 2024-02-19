import numpy as np
from numpy import linalg
import numpy as np

A = np.array([[2, 2, 0], 
              [1, -1, 1],
              [4, 2, -2]])
b = np.array([0, 0, 0])
c = np.linalg.solve(A,b)
print(c)

[0., -0.,  0.]

D = np.array([[2, -2, 2], 
              [1, -1, 1],
              [4, 2, -2]])
e = np.array([0, 0, 0])
f = np.linalg.solve(D,f)
print(f)
# You should get many lines indicating an error. Among the spew, you should see:
# raise LinAlgError("Singular matrix")

G = np.array([[4, 3, -5], 
              [-2, -4, 5], 
              [8, 8, 0]])
h = np.array([2, 5, -3])

j = np.linalg.solve(G, h)
print(j)

if (np.linalg.det(D) != 0):
    j = np.linalg.solve(D,e)
    print(j)
else:
     print("Rows and columns are not independent.")
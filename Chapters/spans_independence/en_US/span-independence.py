// import the python module that supports matrices
import numpy as np
from numpy import linalg

z1 = np.array([2,1,4])
z2 = np.array([2,-1,2])
z3 = np.array([0,1,-2])
d = np.array([z1,z2,z3])
ans = np.linalg.det(d)
print(ans)

// should be 12 i.e., not equal to zero so linearly independent

z1 = np.array([1,1,1])
z2 = np.array([0,1,-1])
z3 = np.array([1,2,0])
d = np.array([z1,z2,z3])
ans = np.linalg.det(d)
print(ans)

// should be 0 so linearly dependent
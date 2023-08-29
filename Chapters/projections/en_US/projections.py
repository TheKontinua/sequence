# import numpy to perform operations on vector
import numpy as np
  
a = np.array([1, 4, 6])   # vector a
b = np.array([-2, 6, 2])   # vector b:
  
# Find the norm of vector b
b_norm = np.sqrt(sum(b**2))    
  
# Find the projection
# Use np.dot() to calculate the dot product
projection_a_on_b = (np.dot(a, b)/b_norm**2)*b
  
print("The projection of vector a on vector b is: ", projection_a_on_b)

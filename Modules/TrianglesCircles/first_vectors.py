import numpy as np

# Create two vectors
v = np.array([2,3,4])
u = np.array([-1,-2,3])
print(f"u = {u}, v = {v}")

# Add them
w = v + u
print(f"u + v = {w}")

# Multiply by a scalar
w = v * 3
print(f"v * 3 = {w}")

# Get the magnitude
mv = np.linalg.norm(v)
mu = np.linalg.norm(u)
print(f"|v| = {mv:.2f}, |u| = {mu:.2f}")

# Take the dot product
d = v @ u
print("v @ u =", d)

# Get the angle between the vectors
a = np.arccos(d / (mv * mu))
print(f"The angle between u and v is {a * 180 / np.pi:.2f} degrees")


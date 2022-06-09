import numpy as np
import matplotlib.pyplot as plt

# Constants
mass = 100 # kg
spring_constant = -1 # newtons per meter displacement
time_step = 0.01 # s

# Initial state
displacement = 1.0 # height above equilibrium in meters
velocity = 0.0
time = 0.0 # seconds

# Lists to gather data
displacements = []
times = []

# Run it for a little while
while time <= 8.0:
    # Record data
    displacements.append(displacement)
    times.append(time)

    # Calculate the next state
    time += time_step
    displacement += time_step * velocity
    force = spring_constant * displacement 
    acceleration = force / mass
    velocity += acceleration

# For comparison, make a plot of cosine
thetas = np.linspace(0, 8, 32)
cosines = []
for theta in thetas:
    cosines.append(np.cos(theta))

# Plot the data
fig, ax = plt.subplots()
ax.plot(times, displacements, 'b', label="Displacement")
ax.plot(thetas, cosines, 'r.', label="Cosine")

ax.set_title("Weight on Spring vs. Cosine")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Displacement (m)")
ax.legend()
plt.show()



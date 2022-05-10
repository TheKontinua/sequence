import numpy as np
import matplotlib.pyplot as plt

# Constants
mass = 45 # kg
muzzle_velocity = 300.0 # m/s
theta = np.pi/5 # radians (36 degrees above level)
time_step = 0.01 # s
wind_resistance = 0.05 # newtons in 1 m/s wind
force_of_gravity = np.array([0.0, -9.8 * mass]) # newtons

# Initial state
position = np.array([0.0, 0.0]) # [distance, height] in meters
velocity = np.array([muzzle_velocity * np.cos(theta), muzzle_velocity * np.sin(theta)])
time = 0.0 # seconds

# Lists to gather data
distances = []
heights = []
times = []

# While shell is aloft
while position[1] >= 0:
    # Record data
    distances.append(position[0])
    heights.append(position[1])
    times.append(time)

    # Calculate the next state
    time += time_step
    position += time_step * velocity

    # Calculate the net force vector
    force = force_of_gravity - wind_resistance * velocity**2

    # Calculate the current acceleration vector
    acceleration = force / mass

    # Update the velocity vector   
    velocity += time_step * acceleration

print(f"The shell hit the ground {position[0]:.2f} meters away at {time:.2f} seconds.")

# Plot the data
fig, ax = plt.subplots()
ax.plot(distances, heights)
ax.set_title("Distance vs. Height")
ax.set_xlabel("Distance (m)")
ax.set_ylabel("Height (m)")
plt.show()



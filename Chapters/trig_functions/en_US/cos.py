import numpy as np
import matplotlib.pyplot as plt

# Make a plot of cosine
thetas = np.linspace(0, 8, 32)
cosines = []
for theta in thetas:
    cosines.append(np.cos(theta))

# Plot the data
fig, ax = plt.subplots()
ax.plot(thetas, cosines, 'r.', label="Cosine")
ax.set_title("Cosine")
plt.show()



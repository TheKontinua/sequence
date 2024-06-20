import numpy as np
import pickle
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

length_limits = (7.0, 23.0)
weight_limits = (0.2, 4.4)

# Read the data
with open("data.pkl", "rb") as f:
    fish_dict = pickle.load(f)

fish_names = list(fish_dict.keys())
colors = ["red", "green", "blue"]

# Prepare the data for plotting
n = 0
fish_colors = {}
fish_data = {}
fish_mu = {}
fish_cov = {}
for i, fish_name in enumerate(fish_names):
    a = np.array(fish_dict[fish_name])
    n += a.shape[0]
    fish_data[fish_name] = a
    color_tuple = colors[i]
    fish_colors[fish_name] = color_tuple
    fish_mu[fish_name] = a.mean(axis=0)
    fish_cov[fish_name] = np.cov(a, rowvar=False)
print("*** Mean ***")
print(fish_mu)
print("\n**** Covariance ***")
print(fish_cov)

# Make the plot
fig, axis = plt.subplots(figsize=(10, 10))
axis.set_title(f"Fish We Measured (n={n})")
axis.set_xlabel("length (cm)")
axis.set_ylabel("weight (kg)")
axis.set_xlim(length_limits)
axis.set_ylim(weight_limits)

# Levels
levels = [0.01 * x for x in range(8)]

for fish_name in fish_names:

    # Grab the data for this breed
    a = fish_data[fish_name]
    count = a.shape[0]
    c = fish_colors[fish_name]

    # Make a scatter plot
    axis.scatter(
        a[:, 0], a[:, 1], label=f"{fish_name} (n={count})", color=c, marker="+"
    )

    # Get the stats for a multivariate normal
    mu = fish_mu[fish_name]
    cov = fish_cov[fish_name]

    # Compute the prior
    p = count / n

    # Make a contour plot
    x, y = np.mgrid[
        length_limits[0] : length_limits[1] : 0.1,
        weight_limits[0] : weight_limits[1] : 0.1,
    ]
    rv = multivariate_normal(mu, cov)
    data = np.dstack((x, y))
    z = rv.pdf(data) * p
    axis.contour(x, y, z, levels, colors=c, alpha=0.5)

# Add a legend to the plot
axis.legend()

fig.savefig("5_full.png")
plt.show()

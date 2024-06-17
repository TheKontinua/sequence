import numpy as np
import pickle
import matplotlib.pyplot as plt
from scipy.stats import norm

length_lims = (7.0, 23.0)
weight_lims = (0.2, 4.4)

# Read the data
with open("data.pkl", "rb") as f:
    fish_dict = pickle.load(f)

# What are the names of the breeds?
fish_names = list(fish_dict.keys())

# What colors will they get?
colors = ["red", "green", "blue"]

# Prepare the data for plotting
n = 0
fish_colors = {}
fish_data = {}
fish_mu = {}
fish_var = {}
for i, fish_name in enumerate(fish_names):
    a = np.array(fish_dict[fish_name])
    n += a.shape[0]
    fish_data[fish_name] = a
    color_tuple = colors[i]
    fish_colors[fish_name] = color_tuple
    fish_mu[fish_name] = a.mean(axis=0)
    fish_var[fish_name] = a.var(axis=0)

print("*** Means ***")
print(fish_mu)
print("\n*** Variance ****")
print(fish_var)

# Make the plot
fig, axis = plt.subplots(2, 1, figsize=(10, 10))
axis[0].set_title(f"Fish We Measured (n={n})")

# Top axis will show length
axis[0].set_xlabel("length (cm)")
axis[0].set_xlim(length_lims)
axis[0].set_ylabel("Probability Density: p(L | F)")
lengths = np.linspace(length_lims[0], length_lims[1], num=200)

# Bottom axis will show weight
axis[1].set_xlabel("weight (kg)")
axis[1].set_xlim(weight_lims)
axis[1].set_ylabel("Probability Density: P(W | F)")
weights = np.linspace(weight_lims[0], weight_lims[1], num=200)

# Loop through the fish
for fish_name in fish_names:

    # Get the data
    a = fish_data[fish_name]

    # Draw the fish data points along the bottom
    count = a.shape[0]
    xs = [-0.01] * count
    c = fish_colors[fish_name]
    axis[0].scatter(a[:, 0], xs, color=c, marker="+")

    # Get the stats
    p = count / n
    mu = fish_mu[fish_name]
    std = np.sqrt(fish_var[fish_name])

    # Plot a normal distribution for the length on axis 0
    y = norm.pdf(lengths, loc=mu[0], scale=std[0])
    axis[0].plot(lengths, y, color=c, label=f"{fish_name} (n={count})")
    v_points = np.array([mu[0] - std[0], mu[0], mu[0] + std[0]])
    tops = norm.pdf(v_points, loc=mu[0], scale=std[0])
    axis[0].vlines(v_points, 0, tops, color=c, linestyle="--", lw=0.5)

    # Plot a normal distribution for the weight on axis 1
    axis[1].scatter(a[:, 1], xs, color=c, marker="+")
    y = norm.pdf(weights, loc=mu[1], scale=std[1])
    axis[1].plot(weights, y, color=c)
    v_points = np.array([mu[1] - std[1], mu[1], mu[1] + std[1]])
    tops = norm.pdf(v_points, loc=mu[1], scale=std[1])
    axis[1].vlines(v_points, 0, tops, color=c, linestyle="--", lw=0.5)

axis[0].legend()
fig.savefig("2_unip.png")
plt.show()

from scipy.stats import multivariate_normal
import numpy as np
import pickle
import random

# How many individuals?
N = 300

# The kinds of fish
fish = ["trout", "bass", "catfish"]

fish_params = {
    "trout": {
        "mu": np.array([13, 1.8]),
        "sigma": np.array([[4, 0.2], [0.2, 0.2]]),
        "p": 0.4,
    },
    "bass": {
        "mu": np.array([18, 2.0]),
        "sigma": np.array([[4.5, 0.45], [0.45, 0.4]]),
        "p": 0.5,
    },
    "catfish": {
        "mu": np.array([17, 3.5]),
        "sigma": np.array([[2, 0.05], [0.05, 0.1]]),
        "p": 0.1,
    },
}

for fish_name in fish:
    print(
        f"{fish_name}: mu={fish_params[fish_name]['mu']} sigma=\n{fish_params[fish_name]['sigma']}"
    )

# Make a dictionary to hold values
fish_data = {}
fish_weights = []
for fish_name in fish:
    fish_data[fish_name] = []
    fish_weights.append(fish_params[fish_name]["p"])

# Make a data point for each fish
for i in range(N):
    fish_name = random.choices(fish, weights=fish_weights)[0]
    params = fish_params[fish_name]
    x = multivariate_normal.rvs(mean=params["mu"], cov=params["sigma"], size=1)
    fish_data[fish_name].append(x)

# Save it in a pickle file
with open("data.pkl", "wb") as f:
    pickle.dump(fish_data, f)

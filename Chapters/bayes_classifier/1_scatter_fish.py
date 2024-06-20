import numpy as np
import pickle
import matplotlib.pyplot as plt

# Read the data
with open("data.pkl", "rb") as f:
    fish_dict = pickle.load(f)

fish_names = list(fish_dict.keys())
colors = ["red", "green", "blue"]

xlims = (7.0, 23.0)
ylims = (0.2, 4.4)


# Prepare the data for plotting
n = 0
fish_colors = {}
fish_data = {}
fish_mu = {}
for i, fish_name in enumerate(fish_names):
    a = np.array(fish_dict[fish_name])
    n += a.shape[0]
    fish_data[fish_name] = a
    fish_colors[fish_name] = colors[i]
    fish_mu[fish_name] = a.mean(axis=0)

# Make the plot
fig, axis = plt.subplots(figsize=(10, 10))
axis.set_title(f"Fish We Measured (n={n})")
axis.set_xlabel("length (cm)")
axis.set_ylabel("weight (kg)")
axis.set_xlim(xlims)
axis.set_ylim(ylims)


for fish_name in fish_names:
    a = fish_data[fish_name]
    c = fish_colors[fish_name]
    count = a.shape[0]
    axis.scatter(a[:, 0], a[:, 1], label=f"{fish_name} (n={count})", c=c, marker="+")
    mu = fish_mu[fish_name]
    axis.axvline(mu[0], color=c, linestyle="--", lw=0.5)
    axis.axhline(mu[1], color=c, linestyle="--", lw=0.5)

axis.legend()

fig.savefig("1_scatter.png")
plt.show()

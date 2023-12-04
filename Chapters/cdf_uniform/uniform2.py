import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1, figsize=(7, 4), dpi=200)
ax.set_ylim(bottom=-0.002, top=4)
ax.set_xlim(left=0.5, right=1.00)
x_s = [0.6, 0.9]
y_s = [10 / 3, 10 / 3]
ax.fill_between(x_s, y_s, color="b", alpha=0.2)
ax.plot(x_s, y_s, "b-", lw=2)

x_s = [0.5, 0.6]
y_s = [0, 0]
ax.plot(x_s, y_s, "b-", lw=2)
x_s = [0.9, 1.0]
y_s = [0, 0]
ax.plot(x_s, y_s, "b-", lw=2)
ax.set_title("PDF of Uniform Distribution (a=0.6, b=0.9)")
ax.set_xlabel("x")
ax.set_ylabel("Probability Density")
fig.savefig("unif_pdf2.png")

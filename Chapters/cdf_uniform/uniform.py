import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1, figsize=(7, 4), dpi=200)
ax.set_ylim(bottom=-0.002, top=1.003)
ax.set_xlim(left=5, right=10.0)
x_s = [5, 6,9,10]
y_s = [0,0,1,1]
ax.plot(x_s, y_s, "b-", lw=2)
ax.scatter(x_s, y_s)
ax.set_title("CDF of Uniform Distribution (a=6, b=9)")
ax.set_xlabel("x")
ax.set_ylabel("Probability")
fig.savefig("unif_cdf.png")

fig, ax = plt.subplots(1, 1, figsize=(7, 4), dpi=200)
ax.set_ylim(bottom=-0.002, top=0.4)
ax.set_xlim(left=5, right=10.0)
x_s = [6, 9]
y_s = [1/3,1/3]
ax.fill_between(x_s, y_s, color="b", alpha=0.2)
ax.plot(x_s, y_s, "b-", lw=2)

x_s = [5, 6]
y_s = [0,0]
ax.plot(x_s, y_s, "b-", lw=2)
x_s = [9,10]
y_s = [0,0]
ax.plot(x_s, y_s, "b-", lw=2)
ax.set_title("PDF of Uniform Distribution (a=6, b=9)")
ax.set_xlabel("x")
ax.set_ylabel("Probability Density")
fig.savefig("unif_pdf.png")
import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt

a = 9
loc = 400
scale = 20
n = 10
bound_min = 620
bound_max = 635

xmin = gamma.ppf(0.01, a, loc=loc, scale=scale) - 30
xmax = gamma.ppf(0.99, a, loc=loc, scale=scale) + 30

cow_weights = gamma.rvs(7.5, loc=loc, scale=scale, size=n)
for i in range(n):
    print(f"Cow {i +1} & {cow_weights[i]:.2f} \\\\")

cow_mass_sorted = np.sort(cow_weights)
proportions = []
masses = []
masses.append(xmin)
proportions.append(0.0)
for i in range(n):
    p = i / n
    m = cow_mass_sorted[i]
    print(f"{p:.2f} & {m:.2f} \\\\")
    proportions.append(p)
    masses.append(m)
    proportions.append(p + 1 / n)
    masses.append(m)
masses.append(xmax)
proportions.append(1.0)

fig, ax = plt.subplots(1, 1, figsize=(7, 4), dpi=200)
ax.set_ylim(bottom=0.0, top=1.0)
ax.set_xlim(left=xmin, right=xmax)
ax.plot(masses, proportions, "b-", lw=1)
ax.set_title("How Many Of My Cows Are Lighter? (n=10)")
ax.set_xlabel("Mass in kg")
ax.set_ylabel("Proportion of my cows lighter")
fig.savefig("cow_sample_cdf.png")

x = np.linspace(xmin, xmax, 200)
fig, ax = plt.subplots(1, 1, figsize=(7, 4), dpi=200)
ax.set_ylim(bottom=0.0, top=1.0)
ax.set_xlim(left=xmin, right=xmax)

ax.plot(x, gamma.cdf(x, a, loc=loc, scale=scale), "b-", lw=1)
ax.set_title("Cow Mass Cumulative Distribution Function")
ax.set_xlabel("Mass in kg")
ax.set_ylabel("Probability a random cow is lighter")
fig.savefig("cow_cdf.png")

bcdf_min = gamma.cdf(bound_min, a, loc=loc, scale=scale)
bcdf_max = gamma.cdf(bound_max, a, loc=loc, scale=scale)

x = np.linspace(xmin, xmax, 200)
fig, ax = plt.subplots(1, 1, figsize=(7, 4), dpi=200)
ax.set_ylim(bottom=0.0, top=1.0)
ax.set_xlim(left=xmin, right=xmax)

ax.plot(x, gamma.cdf(x, a, loc=loc, scale=scale), "b-", lw=1)
ax.vlines(bound_min, 0, bcdf_min, "k", linestyles="dashed")
ax.text(bound_min - 31, 0.2, f"{bound_min:.0f} kg")
ax.hlines(bcdf_min, xmin, bound_min, "k", linestyles="dashed")
ax.text(500, bcdf_min - 0.04, f"{bcdf_min:.2f}")

ax.vlines(bound_max, 0, bcdf_max, "k", linestyles="dashed")
ax.text(bound_max + 2, 0.2, f"{bound_max:.0f} kg")
ax.hlines(bcdf_max, xmin, bound_max, "k", linestyles="dashed")
ax.text(500, bcdf_max + 0.01, f"{bcdf_max:.2f}")


ax.set_title("Cow Mass Cumulative Distribution Function")
ax.set_xlabel("Mass in kg")
ax.set_ylabel("Probability a random cow is lighter")
fig.savefig("cow_cdf_bounds.png")

x = np.linspace(xmin, xmax, 200)
fig, ax = plt.subplots(1, 1, figsize=(7, 4), dpi=200)
ax.set_xlim(left=xmin, right=xmax)
ax.set_ylim(bottom=0, top=0.0075)

ax.plot(x, gamma.pdf(x, a, loc=loc, scale=scale), "b-", lw=1)
ax.set_xlabel("Mass in kg")
ax.set_ylabel("Probability Density")
ax.set_title("Cow Mass Probability Distribution Function")
fig.savefig("cow_pdf.png")

bpdf_min = gamma.pdf(bound_min, a, loc=loc, scale=scale)
bpdf_max = gamma.pdf(bound_max, a, loc=loc, scale=scale)
pdfs = gamma.pdf(x, a, loc=loc, scale=scale)

mle = np.argmax(pdfs)
print(f"{x[mle]}")

x = np.linspace(xmin, xmax, 200)
fig, ax = plt.subplots(1, 1, figsize=(7, 4), dpi=200)
ax.set_xlim(left=xmin, right=xmax)
ax.set_ylim(bottom=0, top=0.0075)

ax.plot(x, pdfs, "b-", lw=1)
ax.vlines(bound_min, 0, bpdf_min, "k", linestyles="dashed")
ax.text(bound_min - 31, 0.0015, f"{bound_min:.0f} kg")

ax.vlines(bound_max, 0, bpdf_max, "k", linestyles="dashed")
ax.text(bound_max + 2, 0.0015, f"{bound_max:.0f} kg")

small_x = np.linspace(bound_min, bound_max, 40)
ax.fill_between(
    small_x, gamma.pdf(small_x, a, loc=loc, scale=scale), color="b", alpha=0.1
)

ax.set_xlabel("Mass in kg")
ax.set_ylabel("Probability Density")
ax.set_title("Cow Mass Probability Distribution Function")
fig.savefig("cow_pdf_bounds.png")

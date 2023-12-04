import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, beta

p = 0.62
n = 12

k_values = np.array(range(n))
f_k = binom.pmf(k_values, n, p)

for i in range(n):
    print(f"{k_values[i]} & {f_k[i]:3f} \\\\")

fig, ax = plt.subplots(1, 1, figsize=(6, 4), dpi=288)
ax.bar(k_values, f_k, align='center')
ax.set_xlabel('k')
ax.set_ylabel('p(k)')
ax.set_title(f"Probability of k positives (r={p:.2f}, n={n})")

fig.savefig('binomial_dist.png')

k = 9
print(f"10 percent: {binom.pmf(k, n, 0.1):.9f}")
print(f"70 percent: {binom.pmf(k, n, 0.7):.9f}")

r_values = np.linspace(0,1,200)
p_values = binom.pmf(k, n, r_values)

fig, ax = plt.subplots(1, 1, figsize=(8, 5), dpi=200)
ax.set_xlim(left=0, right=1.0)
ax.set_ylim(bottom=0, top=0.27)
ax.plot(r_values, p_values, "b")
ax.set_xlabel('r')
ax.set_ylabel('p(10)')
ax.set_title(f"Likelihood of 9 positives (n={n})")
fig.savefig('likelihood.png')

p_values = beta.pdf(r_values, k+1, n-k+1)

fig, ax = plt.subplots(1, 1, figsize=(8, 5), dpi=200)
ax.set_xlim(left=0, right=1.0)
ax.set_ylim(bottom=0, top=3.5)
ax.plot(r_values, p_values, "b")
ax.set_xlabel('r')
ax.set_ylabel('p(r)')
ax.set_title(f"Probability Density")
fig.savefig('bayes.png')

sub_rs = np.linspace(0.5,1,100)
sub_ps = beta.pdf(sub_rs, k+1, n-k+1)

fig, ax = plt.subplots(1, 1, figsize=(8, 5), dpi=200)
ax.set_xlim(left=0, right=1.0)
ax.set_ylim(bottom=0, top=3.5)
ax.fill_between(sub_rs, sub_ps, color="b", alpha=0.2)
ax.plot(r_values, p_values, "b")
ax.set_xlabel('r')
ax.set_ylabel('p(r)')
ax.set_title(f"Probability Density")
fig.savefig('bayes50.png')


p_values = beta.pdf(r_values, k * 10 +1, n * 10 - k * 10 +1)

fig, ax = plt.subplots(1, 1, figsize=(8, 5), dpi=200)
ax.set_xlim(left=0, right=1.0)
ax.set_ylim(bottom=0, top=11)
ax.plot(r_values, p_values, "b")
ax.set_xlabel('r')
ax.set_ylabel('p(r)')
ax.set_title(f"Probability Density")
fig.savefig('bayes_tight.png')


p_less = beta.cdf(0.5, k +1, n - k +1)
p_more = 1.0 - p_less
print(f"I'm {p_more * 100.0:.2f}% sure you will win.")
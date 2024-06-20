import numpy as np
import pickle
from scipy.stats import multivariate_normal
import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <length> <weight>")
    exit(-1)

length_in = float(sys.argv[1])
weight_in = float(sys.argv[2])
data_point = np.array([length_in, weight_in])

# Read the data
with open("data.pkl", "rb") as f:
    fish_dict = pickle.load(f)

fish_names = list(fish_dict.keys())

# Compute means and variances
n = 0
fish_mu = {}
fish_cov = {}
fish_count = {}
for fish_name in fish_names:
    a = np.array(fish_dict[fish_name])
    count = a.shape[0]
    fish_count[fish_name] = count
    fish_mu[fish_name] = a.mean(axis=0)
    fish_cov[fish_name] = np.cov(a, rowvar=False)
    n += count

total_p = 0.0
joint = {}
for fish_name in fish_names:
    # Compute prior 
    prior = fish_count[fish_name]/n
    print(f"P(fish={fish_name}) = {prior*100.0:.1f}%")

    # Compute likelihood of length_in and weight_in
    rv = multivariate_normal(fish_mu[fish_name], fish_cov[fish_name])
    p_len_weight = rv.pdf(data_point)
    print(f"p(length={length_in:.1f}, weight={weight_in:.1f} | {fish_name}) = {p_len_weight*100.0:.3f}%")

    # Compute the joint likelihood
    p = prior * p_len_weight
    print(f"p(fish={fish_name}, length={length_in:.1f}, weight={weight_in:.1f} ) = {p*100.0:.3f}%\n")

    # Note the joint
    joint[fish_name] = p

    # Update the sum of all joint probabilities
    total_p += p

print(f"p(length={length_in:.1f}, weight={weight_in:.1f} ) = {total_p*100.0:.2f}%\n")

max_p = 0.0
for fish_name in fish_names:
    p = joint[fish_name]/total_p
    print(f"p(fish={fish_name} | length={length_in:.1f}, weight={weight_in:.1f} ) = {p*100.0:.1f}%")
    if p > max_p:
        best_guess = fish_name
        max_p = p
print(f"\nPrediction: {best_guess}, with {max_p*100.0:.1f}% confidence.")





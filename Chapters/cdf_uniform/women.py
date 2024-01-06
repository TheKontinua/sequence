from scipy.stats import norm

# Constants
MEAN = 164.7 
STD = 7.1

# What is the cutoff for the top decile?
cutoff = norm.ppf(0.9, loc=MEAN, scale=STD);
print(f"To be in the top 10 percent, you must be at least {cutoff:.2f} cm")

# What proportion of women are between 160cm and 165cm?
shorter_than_160 = norm.cdf(160, loc=MEAN, scale=STD)
shorter_than_165 = norm.cdf(165, loc=MEAN, scale=STD)
between = shorter_than_165 - shorter_than_160
print(f"{between * 100.0:.2f}% of adult women are between 160 and 165 cm.")
from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np

a = 2
b = 5
min_speed = 24.0
spread = 27.0

print(f"Min: {min_speed:.2f}, Spread: {spread:.2f}")

mean = min_speed + spread * (a / (a + b))
print(f"Theoretical Mean: {mean:.2f} m/s")

median = min_speed + spread * (a - 1.0/3.0) / (a + b - 2.0/3.0)
print(f"Approximate theoretical median: {median:.2f} m/s")

mode = min_speed + spread * (a - 1)*(a + b -2)
print(f"Theoretical mode: {mode:.2f} m/s")

variance =  spread * spread * (a*b)/((a + b)^2 * (a + b + 1))
print(f"Theoretical Variance: {variance:.2f}")

samples = min_speed + spread * beta.rvs(a, b, size=1000)

print(f"samples: {samples[:12]}")

print(f"Actual mean: {np.mean(samples)}")

print(f"Actual variance: {np.var(samples)}")

fig, ax = plt.subplots()
ax.set_ylabel('Number of cars')
ax.set_xlabel('Speed in m/s')
# labels = []
# for i in range(0,50,4):
#    labels.append(f"{i}-{i+2}")
#    
# x = np.arange(len(labels))
# ax.set_xticks(x, labels=labels)

bins = range(0,54,2)
(counts_out, bins_out, _) = ax.hist(samples, bins=bins, density=False, histtype='stepfilled')

for i in range(len(counts_out)):
    print(f"{bins_out[i]} - {bins_out[i+1]} m/s & {counts_out[i]:.0f} cars \\\\")

plt.show()



// import the python module that supports matrices
import numpy as np

// Create an array for number of umbrellas by manufacturer
items = np.array([100, 50, 200])

// weights are the cost of item by manufacturer
weights = np.array([2.10, 1.85, 2.00])

// create an array for total cost for each manufacturer
cost_per_manufacturer=items * weights

total_cost = np.sum(cost_per_manufacturer)
// get number of items
num_items = np.sum(items) 

weighted_average = total_cost/num_items
print(weighted_average)
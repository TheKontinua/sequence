from Polynomial import Polynomial
import matplotlib.pyplot as plt

# in_x = [2,3,4]
# in_y = [5,7,6]
in_x = [1.7, 2, 2.7, 3.5, 4, 4.4]
in_y = [8, 12, 1, 4, -1, 6]
# pn = Polynomial([-8, 19/2, -3/2])
pn = Polynomial.from_points(in_x, in_y)
print(pn)

# These lists will hold our x and y values
x_list = []
y_list = []

current_x = 1.5

while current_x <= 4.5:
    current_y = pn(current_x)

    # Add x and y to respective lists
    x_list.append(current_x)
    y_list.append(current_y)

    # Move x forward
    current_x += 0.05

# Plot the curve
plt.plot(x_list, y_list)

# Plot the points
plt.plot(in_x, in_y, "ko")
plt.grid(True)
plt.show()



import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 1, 5, 4])
quantities = np.array([10, 20, 15, 25, 30])

plt.scatter(x, y, s=60)
for xi, yi, qi in zip(x, y, quantities):
    plt.text(xi, yi, str(qi), ha="center", va="bottom")

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Quantities at Positions")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 6)
y = np.array([2, 1, 4, 3, 5])

fig, ax = plt.subplots()
ax.plot(x, y)
print("Current x limits:", ax.get_xlim())
print("Current y limits:", ax.get_ylim())

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Axis Limits Example")

plt.show()

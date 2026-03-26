import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 6)
y1 = x
y2 = x**2
y3 = np.sqrt(x)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(x, y1)
axes[0, 0].set_title("Plot 1")
axes[0, 0].set_xlabel("X")
axes[0, 0].set_ylabel("Y")

axes[0, 1].plot(x, y2)
axes[0, 1].set_title("Plot 2")
axes[0, 1].set_xlabel("X")
axes[0, 1].set_ylabel("Y")

axes[1, 0].plot(x, y3, marker="o")
axes[1, 0].set_title("Plot 3")
axes[1, 0].set_xlabel("X")
axes[1, 0].set_ylabel("Y")

axes[1, 1].bar(x, y1 + y3)
axes[1, 1].set_title("Plot 4")
axes[1, 1].set_xlabel("X")
axes[1, 1].set_ylabel("Value")

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 6)
y_line = x**2
y_bar = x**3
y_scatter = np.sqrt(x)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(x, y_line)
axes[0].set_title("Line Chart")
axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")

axes[1].bar(x, y_bar)
axes[1].set_title("Bar Chart")
axes[1].set_xlabel("X")
axes[1].set_ylabel("Y")

axes[2].scatter(x, y_scatter)
axes[2].set_title("Scatter Chart")
axes[2].set_xlabel("X")
axes[2].set_ylabel("Y")

plt.tight_layout()
plt.show()

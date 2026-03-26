import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 6)
y1 = x
y2 = x**2

plt.plot(x, y1, marker="o", linestyle="-", label="Circle Marker")
plt.plot(x, y2, marker="s", linestyle="-", label="Square Marker")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line Chart With Markers")
plt.legend()
plt.show()

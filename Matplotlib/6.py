import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 6)
y1 = x
y2 = x**2

plt.plot(x, y1, label="Red Line", color="red", linewidth=1)
plt.plot(x, y2, label="Green Line", color="green", linewidth=3)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line Chart With Different Widths and Colors")
plt.legend()
plt.show()

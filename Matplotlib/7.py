import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 6)
y1 = x
y2 = x**2
y3 = x**0.5

plt.plot(x, y1, linestyle="--", label="Dashed")
plt.plot(x, y2, linestyle=":", label="Dotted")
plt.plot(x, y3, linestyle="-.", label="Dash-Dot")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line Chart With Different Styles")
plt.legend()
plt.show()

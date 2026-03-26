import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 6)
y1 = x
y2 = x**2
y3 = 1 / x

plt.plot(x, y1, "r--o", x, y2, "g-^", x, y3, "b:d")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Several Lines With Different Formats")
plt.show()

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

data_path = Path(__file__).with_name("test.txt")
data = np.loadtxt(data_path)
x = data[:, 0]
y = data[:, 1]

plt.plot(x, y)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Chart From Text File")
plt.show()

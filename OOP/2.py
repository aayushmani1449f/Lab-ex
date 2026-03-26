import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'x': np.arange(10),
    'y': np.random.randint(0, 20, size=10)
})

plt.plot(data['x'], data['y'], marker='o', color='green')
plt.title('Sample Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
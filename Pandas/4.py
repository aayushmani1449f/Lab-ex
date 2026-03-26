import numpy as np

a = np.array([0, 1, 2, 3, 4, 5, 6])
b = np.array([1, 1, 3, 3, 3, 3, 3])

print("Original array")
print(a)
print("First array elements raised to powers from second array, element-wise:")
print(np.power(a, b))


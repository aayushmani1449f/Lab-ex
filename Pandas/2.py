import pandas as pd

series = pd.Series([2, 4, 6, 8, 10])

py_list = series.tolist()

print(py_list)
print(type(py_list))


from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

data_path = Path(__file__).with_name("fdata.csv")
df = pd.read_csv(data_path)
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%y")

start_date = pd.to_datetime("2016-10-03")
end_date = pd.to_datetime("2016-10-07")
df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)].sort_values("Date")

plt.plot(df["Date"], df["Open"], label="Open")
plt.plot(df["Date"], df["High"], label="High")
plt.plot(df["Date"], df["Low"], label="Low")
plt.plot(df["Date"], df["Close"], label="Close")

plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Alphabet Inc. Financial Data (Oct 3 to Oct 7, 2016)")
plt.legend()
plt.show()

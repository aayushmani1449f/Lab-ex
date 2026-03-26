from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

data_path = Path(__file__).with_name("fdata.csv")
df = pd.read_csv(data_path)
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%y")

start_date = pd.to_datetime("2016-10-03")
end_date = pd.to_datetime("2016-10-07")
df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)].sort_values("Date")

fig, ax = plt.subplots()
ax.plot(df["Date"], df["Close"])

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

ax.grid(which="major", linestyle="-", linewidth=1.0, color="blue")
ax.grid(which="minor", linestyle="-", linewidth=0.2, color="lightblue")

ax.tick_params(
    which="both",
    bottom=False,
    top=False,
    left=False,
    right=False,
    labelbottom=False,
    labelleft=False,
)

ax.set_xlabel("Date")
ax.set_ylabel("Close Price")
ax.set_title("Alphabet Inc. Close (Oct 3 to Oct 7, 2016) - Major/Minor Grid")

plt.show()

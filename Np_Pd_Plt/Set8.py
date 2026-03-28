import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from faker import Faker

random.seed(42)
np.random.seed(42)
Faker.seed(42)

cities = ["North", "South", "East", "West", "Central"]
st = ["completed", "cancelled", "no_show"]
rows = []
for i in range(1, 521):
    c = random.choice(cities)
    h = random.randint(0, 23)
    peak = 7 <= h <= 9 or 17 <= h <= 20
    w = [0.82, 0.12, 0.06] if peak else [0.75, 0.18, 0.07]
    f = round(random.uniform(12, 55) if peak else random.uniform(8, 40), 2)
    rows.append({"ride_id": f"R{i:06d}", "city": c, "hour": h, "fare": f, "ride_status": random.choices(st, weights=w)[0]})

df = pd.DataFrame(rows)
ch = df.groupby(["city", "hour"]).size().reset_index(name="n")
peak = ch.loc[ch.groupby("city")["n"].idxmax()]
print(peak.to_string(index=False), "\n")
print((df.groupby("city")["ride_status"].apply(lambda s: (s == "cancelled").mean()) * 100).round(2), "\n")

piv = df.groupby(["city", "hour"]).size().unstack(fill_value=0)
idx = piv.div(piv.mean(axis=1), axis=0)
print(idx.shape)
s = piv.loc[cities[0]].reindex(range(24), fill_value=0).values.astype(float)
print(s.sum(), np.argmax(np.convolve(s, np.ones(3) / 3, mode="same")))

fig, ax = plt.subplots(1, 2, figsize=(13, 4))
for c in cities:
    hc = df[df["city"] == c].groupby("hour").size().reindex(range(24), fill_value=0)
    ax[0].plot(hc.index, hc.values, marker=".", label=c, markersize=4)
ax[0].legend(fontsize=8)
vc = df["ride_status"].value_counts()
ax[1].bar(vc.index.astype(str), vc.values, color=["green", "red", "gray"])
plt.tight_layout()
plt.show()

import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from faker import Faker

random.seed(42)
np.random.seed(42)
fake = Faker()
Faker.seed(42)

rest = ["Tasty Bowl", "Pizza Plaza", "Sushi Zen", "Burger Barn", "Taco Town", "Curry House", "Salad Bar"]
rows = []
for i in range(1, 321):
    r = random.choice(rest)
    v = round(random.uniform(12, 85), 2)
    if random.random() < 0.06:
        t = np.nan
    else:
        t = max(5, int(random.gauss(32, 12)))
        if random.random() < 0.03:
            t = -5
        if random.random() < 0.02:
            t = 400
    if np.isnan(t):
        rt = float(np.clip(random.gauss(3.5, 0.9), 1, 5))
    else:
        rt = float(np.clip(random.gauss(4.0 - t / 80, 0.7), 1, 5))
    rows.append({"order_id": f"FD{i:05d}", "restaurant": r, "order_value": v, "delivery_time": t, "customer_rating": round(rt, 2)})

df = pd.DataFrame(rows)
raw = df["delivery_time"].values
ok = raw[(raw == raw) & (raw > 0) & (raw < 180)]
med = float(np.median(ok)) if len(ok) else 30.0
df["delivery_time_clean"] = np.where(np.isnan(raw) | (raw <= 0) | (raw > 180), med, raw)
print(np.percentile(df["delivery_time_clean"], [0, 25, 50, 75, 90, 99]))

rev = df.groupby("restaurant")["order_value"].sum().sort_values(ascending=False)
print(rev, "\n")
perf = df.groupby("restaurant").agg(avg_rating=("customer_rating", "mean"), avg_delivery=("delivery_time_clean", "mean"), n=("order_id", "count"))
perf["score"] = -perf["avg_rating"] + perf["avg_delivery"] / 40
print(perf.sort_values("score", ascending=False).head(4).round(2), "\n")

fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].scatter(df["delivery_time_clean"], df["customer_rating"], alpha=0.5)
top = rev.head(5)
ax[1].barh(top.index.astype(str), top.values, color="orange")
plt.tight_layout()
plt.show()

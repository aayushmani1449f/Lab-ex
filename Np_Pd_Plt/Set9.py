import random
from datetime import timedelta

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from faker import Faker

random.seed(42)
np.random.seed(42)
fake = Faker()
Faker.seed(42)

srcs = ["organic", "paid", "social", "email", "referral"]
mult = {"organic": 1.0, "paid": 0.85, "social": 0.7, "email": 0.9, "referral": 1.1}
d0 = fake.date_between(start_date="-250d", end_date="-200d")
rows = []
for i in range(200):
    s = random.choice(srcs)
    b = mult[s]
    vis = max(200, int(random.gauss(2500 * b, 400)))
    su = int(vis * random.uniform(0.02, 0.08) * b)
    pu = int(su * random.uniform(0.15, 0.35))
    rows.append({"date": d0 + timedelta(days=i), "visits": vis, "signups": su, "purchases": pu, "traffic_source": s})

df = pd.DataFrame(rows)
df["date"] = pd.to_datetime(df["date"])
df["v2s"] = df["signups"] / df["visits"].replace(0, np.nan)
df["s2p"] = np.where(df["signups"] > 0, df["purchases"] / df["signups"], np.nan)
df["v2p"] = df["purchases"] / df["visits"].replace(0, np.nan)
print(df["v2s"].mean() * 100, np.nanmean(df["s2p"]) * 100, df["v2p"].mean() * 100)

agg = df.groupby("traffic_source").agg(p=("purchases", "sum"), v=("visits", "sum"))
rate = agg["p"] / agg["v"]
print(rate.idxmax(), rate.max() * 100)

br = (df["purchases"] / df["visits"]).mean()
rng = np.random.default_rng(42)
sim = np.clip(br + rng.normal(0, 0.15 * br, 500), 0, 0.5)
print(sim.mean(), sim.std())

vp = df.sort_values("date")["v2p"].values
w = 14
bad = sum(1 for i in range(w, len(vp)) if vp[i] < 0.8 * vp[i - w : i].mean())
print(bad / max(1, len(vp) - w))

fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].bar(["Visits", "Signups", "Purchases"], [df["visits"].mean(), df["signups"].mean(), df["purchases"].mean()], color=["#5b9bd5", "#ed7d31", "#a5a5a5"])
ax[1].plot(df["date"], df["v2s"] * 100, label="v2s")
ax[1].plot(df["date"], df["v2p"] * 100, label="v2p")
ax[1].legend()
plt.tight_layout()
plt.show()

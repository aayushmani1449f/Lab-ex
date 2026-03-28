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

p = 100.0
rows = []
d0 = fake.date_between(start_date="-400d", end_date="-300d")
for i in range(260):
    r = random.gauss(0.0005, 0.015)
    o = p * (1 + random.gauss(0, 0.003))
    c = o * (1 + r)
    rows.append({"date": d0 + timedelta(days=i), "open_price": round(o, 4), "close_price": round(c, 4), "volume": int(random.uniform(1e5, 5e6))})
    p = c

df = pd.DataFrame(rows).sort_values("date").reset_index(drop=True)
df["date"] = pd.to_datetime(df["date"])
df["daily_return"] = df["close_price"].pct_change()
df["rolling_volatility"] = df["daily_return"].rolling(20).std() * np.sqrt(252)
print(df[["date", "close_price", "daily_return", "rolling_volatility"]].tail(8).to_string(index=False), "\n")

lc = float(df["close_price"].iloc[-1])
dr = df["daily_return"].dropna().values
mu, sig = dr.mean() * 252, dr.std(ddof=1) * np.sqrt(252)
T, dt, n = 30, 1 / 252, 5000
rng = np.random.default_rng(42)
inc = rng.normal((mu - 0.5 * sig**2) * dt, sig * dt**0.5, size=(n, T))
sim = np.exp(np.log(lc) + np.cumsum(inc, axis=1))
print(sim[:, -1].mean(), "mean terminal")

var = np.percentile(dr, 5)
print(var, dr[dr <= var].mean(), dr.mean() / dr.std(ddof=1) * np.sqrt(252))

fig, ax = plt.subplots(1, 2, figsize=(13, 4))
ax[0].plot(df["date"], df["close_price"])
ax[1].hist(dr, bins=40, density=True, color="steelblue", edgecolor="white", alpha=0.85)
plt.tight_layout()
plt.show()

import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from faker import Faker

random.seed(42)
np.random.seed(42)
fake = Faker()
Faker.seed(42)

cats = ["Electronics", "Clothing", "Home", "Books", "Sports", "Beauty"]
df = pd.DataFrame(
    [
        {
            "order_id": f"ORD{i:05d}",
            "order_date": fake.date_between(start_date="-2y", end_date="today"),
            "customer_id": fake.uuid4()[:10],
            "product_category": random.choice(cats),
            "price": round(random.uniform(10, 500), 2),
            "quantity": random.randint(1, 10),
            "discount_percent": random.choice([0, 5, 10, 15, 20, 25]),
        }
        for i in range(1, 551)
    ]
)
df["order_date"] = pd.to_datetime(df["order_date"])
df["final_amount"] = df["price"] * df["quantity"] * (1 - df["discount_percent"] / 100)
df["year_month"] = df["order_date"].dt.to_period("M").astype(str)

monthly = (
    df.groupby(["year_month", "product_category"], as_index=False)["final_amount"]
    .sum()
    .rename(columns={"final_amount": "revenue"})
)
top3 = df.groupby("product_category")["final_amount"].sum().nlargest(3)
print(top3, "\n")

a = df["final_amount"].values
q1, q3 = np.percentile(a, [25, 75])
lo, hi = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
print(int(((a < lo) | (a > hi)).sum()), "outliers")
df["final_amount_winsorized"] = np.clip(a, lo, hi)

pv = monthly.pivot(index="year_month", columns="product_category", values="revenue").fillna(0).sort_index()
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
for c in pv.columns:
    ax[0].plot(pv.index.astype(str), pv[c].values, marker="o", label=c, markersize=3)
ax[0].legend(fontsize=7, ncol=2)
ax[0].tick_params(axis="x", rotation=45)
tot = df.groupby("product_category")["final_amount"].sum().sort_values(ascending=False)
ax[1].bar(tot.index.astype(str), tot.values, color="steelblue")
ax[1].tick_params(axis="x", rotation=45)
plt.tight_layout()
plt.show()

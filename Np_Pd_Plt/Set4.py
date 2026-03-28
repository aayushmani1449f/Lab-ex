import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from faker import Faker

random.seed(42)
np.random.seed(42)
fake = Faker()
Faker.seed(42)

dx = ["Flu", "Fracture", "Hypertension", "Diabetes", "Appendicitis", "Pneumonia", "Migraine"]
base_days = {"Flu": 3, "Fracture": 7, "Hypertension": 2, "Diabetes": 4, "Appendicitis": 6, "Pneumonia": 8, "Migraine": 1}
rows = []
for i in range(1, 421):
    age = random.randint(1, 90)
    diag = random.choice(dx)
    days = max(1, int(random.gauss(base_days[diag] + age / 40, 2)))
    cost = max(200, days * random.uniform(800, 2500) + random.gauss(0, 2000))
    rows.append(
        {
            "patient_id": f"P{i:05d}",
            "age": age,
            "gender": random.choice(["M", "F", "Other"]),
            "diagnosis": diag,
            "hospital_days": days,
            "treatment_cost": round(cost, 2),
        }
    )
df = pd.DataFrame(rows)

print(df.groupby("diagnosis")["hospital_days"].mean().round(2).sort_values(ascending=False), "\n")
df["age_group"] = pd.cut(df["age"], [0, 18, 35, 55, 75, 120], labels=["0-17", "18-34", "35-54", "55-74", "75+"])
print(df["age_group"].value_counts().sort_index(), "\n")

c = np.log1p(df["treatment_cost"].values)
z = (c - c.mean()) / c.std(ddof=1)
print(int((np.abs(z) > 3).sum()), "cost outliers")
df["cost_log_z"] = z

fig, ax = plt.subplots(1, 2, figsize=(13, 5))
ax[0].boxplot([df.loc[df["diagnosis"] == d, "hospital_days"] for d in dx], tick_labels=dx)
ax[0].tick_params(axis="x", rotation=25)
g = df.groupby("age_group", observed=False)["treatment_cost"].mean()
ax[1].bar(g.index.astype(str), g.values, color="mediumpurple")
ax[1].tick_params(axis="x", rotation=30)
plt.tight_layout()
plt.show()

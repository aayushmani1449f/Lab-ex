import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from faker import Faker

random.seed(42)
np.random.seed(42)
fake = Faker()
Faker.seed(42)

base = {"Engineering": 90000, "Sales": 70000, "HR": 65000, "Finance": 80000, "Operations": 60000, "Marketing": 72000}
depts = list(base.keys())
rows = []
for i in range(1, 221):
    d = random.choice(depts)
    y = random.randint(0, 25)
    sal = max(35000, int(base[d] + y * random.uniform(1500, 3500) + random.gauss(0, 8000)))
    perf = round(float(np.clip(random.gauss(3.5 + y * 0.02, 0.8), 1, 5)), 2)
    rows.append({"emp_id": f"E{i:05d}", "department": d, "experience_years": y, "salary": sal, "performance_score": perf})

df = pd.DataFrame(rows)
print(df.groupby("department").agg(n=("emp_id", "count"), m=("salary", "mean"), p=("performance_score", "mean")).round(2), "\n")

df["salary_band"] = pd.cut(
    df["salary"], [0, 50000, 75000, 100000, 125000, np.inf], right=False,
    labels=["<50k", "50k-75k", "75k-100k", "100k-125k", "125k+"],
)
print(df["salary_band"].value_counts().sort_index(), "\n")

exp, sal, perf = df["experience_years"].values, df["salary"].values, df["performance_score"].values
mm = lambda x: (x - x.min()) / (x.max() - x.min()) if x.max() > x.min() else x * 0
print("norm ranges", mm(exp).min(), mm(sal).max(), mm(perf).min())
print("corr", np.corrcoef(sal, perf)[0, 1], "\n")

fig, ax = plt.subplots(1, 2, figsize=(13, 5))
order = sorted(df["department"].unique())
ax[0].boxplot([df.loc[df["department"] == d, "salary"] for d in order], tick_labels=order)
ax[0].tick_params(axis="x", rotation=30)
ax[1].scatter(df["experience_years"], df["salary"], alpha=0.6, c="teal")
plt.tight_layout()
plt.show()

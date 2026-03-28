import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from faker import Faker

random.seed(42)
np.random.seed(42)
fake = Faker()
Faker.seed(42)

rows = []
for i in range(1, 211):
    att = float(np.clip(random.gauss(82, 12), 50, 100))
    n = (att - 75) * 0.15
    rows.append(
        {
            "student_id": f"S{i:05d}-{fake.uuid4()[:6]}",
            "math": round(float(np.clip(random.gauss(72 + n, 10), 0, 100)), 1),
            "science": round(float(np.clip(random.gauss(70 + n, 11), 0, 100)), 1),
            "english": round(float(np.clip(random.gauss(74 + n, 10), 0, 100)), 1),
            "attendance_percent": round(att, 1),
        }
    )
df = pd.DataFrame(rows)

df["total_score"] = df["math"] + df["science"] + df["english"]
df["average_score"] = df["total_score"] / 3
df["tier"] = pd.cut(df["average_score"], [0, 55, 70, 85, 100], labels=["Needs support", "Average", "Good", "Excellent"])
print(df["tier"].value_counts(), "\n")

m, s, e = df["math"].values, df["science"].values, df["english"].values
df["weighted_score"] = np.round(0.4 * m + 0.35 * s + 0.25 * e, 2)
z = lambda x: (x - x.mean()) / x.std(ddof=1)
df["math_z"], df["science_z"], df["english_z"] = z(m), z(s), z(e)

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].bar(["Math", "Science", "English"], [df["math"].mean(), df["science"].mean(), df["english"].mean()], color=["#4472c4", "#ed7d31", "#70ad47"])
ax[1].scatter(df["attendance_percent"], df["average_score"], alpha=0.55)
plt.tight_layout()
plt.show()

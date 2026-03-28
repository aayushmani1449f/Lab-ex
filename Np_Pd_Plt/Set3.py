import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from faker import Faker

random.seed(42)
np.random.seed(42)
fake = Faker()
Faker.seed(42)

courses = ["Python Basics", "Data Science 101", "Web Dev", "ML Intro", "Cloud Computing", "SQL Mastery", "UI Design"]
rows = []
for _ in range(320):
    c = random.choice(courses)
    k = courses.index(c) % 4
    prog = float(np.clip(random.gauss(72 - k * 5, 18), 5, 100))
    days = max(1, int(random.gauss(25 + (100 - prog) * 0.3, 12)))
    rating = float(np.clip(random.gauss(3.8 + prog / 200, 0.6), 1, 5))
    rows.append(
        {
            "student_id": fake.uuid4()[:12],
            "course_name": c,
            "progress_percent": round(prog, 2),
            "completion_days": days,
            "rating": round(rating, 2),
        }
    )
df = pd.DataFrame(rows)

med = df.groupby("course_name")["progress_percent"].median()
print(med[med < med.median()], "\n")
print(df.groupby("course_name")["completion_days"].mean().round(2), "\n")

d = df["completion_days"].values
print(np.mean(d), np.std(d, ddof=1), np.percentile(d, [5, 50, 95]))
p = df["progress_percent"].values
print(np.mean(np.clip(p * 1.05, 0, 100)), np.mean(np.clip(p * 1.1, 0, 100)))

fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].hist(d, bins=30, color="coral", edgecolor="white")
r = df.groupby("course_name")["rating"].mean().sort_values()
ax[1].barh(r.index.astype(str), r.values, color="seagreen")
plt.tight_layout()
plt.show()

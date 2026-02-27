readings = [[22, None, 25], [None, None, 19], [20, 21, 22]]

valid_days = [[x for x in day if x is not None] for day in readings]

averages = [sum(day) / len(day) if day else 0 for day in valid_days]

print(averages)
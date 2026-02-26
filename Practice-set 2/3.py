readings = [[22, None, 25], [None, None, 19], [20, 21, 22]]

valid_days = list(map(lambda day: list(filter(lambda x: x is not None, day)), readings))

averages = list(map(lambda valid: sum(valid) / len(valid) if valid else 0, valid_days))

print(averages)
readings = [
    {"temp": 32, "unit": "F"},
    {"temp": 20, "unit": "C"},
    {"temp": -200, "unit": "F"},
    {"temp": -500, "unit": "C"}
]

def normalize_to_celsius(reading):
    temp = reading["temp"]
    if reading["unit"] == "F":
        celsius = (temp - 32) * 5.0 / 9.0
    else:
        celsius = temp
        
    if celsius >= -273.15:
        return round(celsius, 2)
    return None

normalized_temps = list(filter(lambda x: x is not None, map(normalize_to_celsius, readings)))

print(normalized_temps)
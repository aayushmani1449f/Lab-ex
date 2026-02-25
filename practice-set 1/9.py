battery = 100
dpm = int(input("Enter drain per minute : "))

min_used = 0
while battery > 0:
    battery = battery- dpm
    min_used = min_used + 1

print(min_used)

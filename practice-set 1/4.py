time = int(input("Enter the time to check signal : "))
time = time %90
if time>=1 and time <=30:
    signal = "RED"


if time >=31 and time <=45:
    signal = "YELLOW"


if time >= 46 and time <=90:
    signal = "GREEN"
    
print(signal)

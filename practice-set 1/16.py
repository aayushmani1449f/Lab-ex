n = int(input("Enter number of flows : "))
capacity = 1000
vol = 0
for i in range(n):
    flow = int(input(f"Enter flow for {i+1} minute"))
    vol = vol+flow
    if vol<=capacity:
        count = i+1
print(count, "minutes to fill")
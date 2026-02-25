distance = int(input())
age = int(input())

fare = distance * 2

if age < 12:
    fare = fare - (fare * 0.50)
elif age >= 60:
    fare = fare - (fare * 0.30)

print(int(fare))
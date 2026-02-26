seats = 40
n = int(input())

for i in range(n):
    request = int(input())
    if request <= seats:
        print("CONFIRMED")
        seats = seats - request
    else:
        print("WAITLISTED")
a = (input("Enter a year : "))
if len(a) == 4:
    year = int(a)
    if year%4 == 0:
        print(a,"is a Leap year")
    else:
        print(a,"is not a leap year")
else:
    print("Provide a valid year")
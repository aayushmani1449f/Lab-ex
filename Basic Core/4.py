a = int(input("Enter the power of 2 (upto 31): "))

if a>31:
    print("Out of bound")
else:
    for i in range(a):
        print(2**i)
B = int(input("Initial balance : "))
N = int(input("Number of transactions : "))

for i in range(N):
    amt = int(input("Enter amount to withdraw : "))
    if amt % 100 == 0 and amt <= B:
        B = B - amt
        print("Transaction successful")
    elif amt %100 != 0:
        print("Enter a multiple of 100")
    else:
        print("Insufficient fund")

print("Remaining balance is : ", B)

units = int(input("Number of units consumed : "))

if units <= 100:
    bill = units * 3

elif units <= 200:
    bill = (units - 100) * 5 + 300

elif units > 200:
    bill = (units - 200) * 8 + 800
    
if units > 300:
    bill = bill + (bill * 0.1)

print(bill)
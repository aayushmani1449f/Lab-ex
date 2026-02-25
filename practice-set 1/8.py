binary = input("Enter binary : ")

decimal = 0
power = 0
for char in binary:
    if char != 0 and char!= 1:
        print("Enter valid binary!!!")
        break
    else:
        binary = int(binary)
        while binary > 0:
            digit = binary % 10
            decimal = decimal + (digit * (2 ** power))
            binary = binary // 10
            power = power + 1
        print(decimal)
number = int(input())
temp = number
reversed_num = 0

while temp > 0:
    digit = temp % 10
    reversed_num = (reversed_num * 10) + digit
    temp = temp // 10

if number == reversed_num:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
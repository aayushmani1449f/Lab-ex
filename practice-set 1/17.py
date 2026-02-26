number = int(input())
temp = number
total = 0

while temp > 0:
    digit = temp % 10
    total = total + (digit ** 3)
    temp = temp // 10

if total == number:
    print("YES")
else:
    print("NO")
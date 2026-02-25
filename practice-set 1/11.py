number = int(input())
count = 0

while number % 2 == 0 and number > 0:
    number = number // 2
    count = count + 1

print(count)
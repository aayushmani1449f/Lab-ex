number = input()
is_increasing = True

for i in range(1, len(number)):
    if number[i] <= number[i-1]:
        is_increasing = False
        break

if is_increasing:
    print("YES")
else:
    print("NO")
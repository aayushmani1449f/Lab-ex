number = int(input())

while number > 9:
    temp = number
    digit_sum = 0
    
    while temp > 0:
        digit = temp % 10
        digit_sum = digit_sum + digit
        temp = temp // 10
        
    number = digit_sum

print(number)
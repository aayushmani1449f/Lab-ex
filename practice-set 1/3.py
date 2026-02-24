password = input("Enter password : ")

has_digit = False
has_upper = False

for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True

if len(password) >= 8 and has_digit and has_upper:
    print("STRONG")
else:
    print("WEAK")
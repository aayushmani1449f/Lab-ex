cp = input("Enter correct PIN : ")

access = False
for i in range(3):
    attempt = input("Enter guess PIN : ")
    if attempt == cp:
        access = True
        break

if access == True:
    print("Access Granted!!")
else:
    print("Access Denied!!")

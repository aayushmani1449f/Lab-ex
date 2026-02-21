rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns"))

arr = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(int(input()))
    arr.append(row)

for row in arr:
    print(*row)


A = int(input("Enter starting range : "))
B = int(input("Enter ending range : "))
arr = []

for i in range(A,B+1):
    count = 0
    for j in range(1,i+1):
        if i % j ==0:
            count=count+1
    if count ==2:
        arr.append(i)
print(len(arr))
            
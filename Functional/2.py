n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

count = 0
triplets = []

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] == 0:
                triplets.append((arr[i], arr[j], arr[k]))
                count += 1

print(count)
for t in triplets:
    print(t[0], t[1], t[2])
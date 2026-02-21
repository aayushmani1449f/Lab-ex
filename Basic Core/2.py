import random


a = int(input("Number of times coin is flipped: "))

heads = 0
tails = 0

for i in range(a):
    if random.random() < 0.5:
        heads = heads+1
    else:
        tails = tails+1

heads_percentage = (heads/a)*100
tails_percentage = (tails/a)*100

print(heads_percentage)
print(tails_percentage)


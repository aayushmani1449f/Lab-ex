marks = input().split()
m1 = int(marks[0])
m2 = int(marks[1])
m3 = int(marks[2])
m4 = int(marks[3])
m5 = int(marks[4])

avg = (m1 + m2 + m3 + m4 + m5) / 5

if m1 < 35 or m2 < 35 or m3 < 35 or m4 < 35 or m5 < 35:
    print("FAIL")
elif avg >= 75:
    print("DISTINCTION")
else:
    print("PASS")
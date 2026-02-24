salary = int(input("Enter base salary : "))
late_days = int(input("Late days : "))
absent_days = int(input("Absent days : "))

if late_days > 5:
    salary = salary*0.95
    if absent_days >2:
        salary = salary*0.95


if late_days > 10:
    salary = salary*0.90
    if absent_days >2:
        salary = salary*0.95
print(salary)
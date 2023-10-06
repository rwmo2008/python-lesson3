rate = int(input("Hourly wage: "))
hours = int(input("Hours worked: "))

if hours <= 40:
    pay = hours * rate
else:
    pay = hours * rate
    overtimeHours = hours - 40
    overtimePay = overtimeHours * (rate * 1.5)
    pay = pay + overtimePay

print("Weekly pay: ", pay)

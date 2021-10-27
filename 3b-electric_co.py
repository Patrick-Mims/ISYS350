#!/usr/bin/python

count = 0
amount = 0

while count < 2:
    used_kwh = int(input("Enter Kilowatt-Hours used: "))
    print(used_kwh)
    if used_kwh <= 50:
        print(".35")
        amount = used_kwh * .035
    elif (used_kwh > 50 and used_kwh <= 150):
        amount += (used_kwh * .035)
        print(".45")
    elif (used_kwh > 150 and used_kwh <= 450):
        amount += (used_kwh * .065)
        print(".65")
    elif (used_kwh > 450 and used_kwh <= 2000):
        amount += (used_kwh * .080)
        print(".80")
    else:
        print("Kilowatt Hours cannot be more than 2000!");

    count = count + 1

print("Kilowatt-Hours used: ",used_kwh,", charge is: ",amount)

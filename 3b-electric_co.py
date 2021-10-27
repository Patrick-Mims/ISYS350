#!/usr/bin/python

count = 0

while count < 6:
    used_kwh = int(input("Enter Kilowatt-Hours used: "))
    print(used_kwh)
    if used_kwh <= 50:
        print(".35")
    elif (used_kwh > 50 and used_kwh <= 150):
        print(".45")
    elif (used_kwh > 150 and used_kwh <= 450):
        print(".65")
    elif (used_kwh > 450):
        print(".80")

    count = count + 1



#!/usr/bin/python
# Name: Patrick Mims
# Class: ISYS-350, Section 2
# Professor: Chao
# Date: 10.27.21
# Extra Credit
# # #

count = 0
amount = 0

while count < 3:
    used_kwh = int(input("Enter Kilowatt-Hours used: "))
    print(used_kwh)
    if used_kwh <= 50:
        print(".35")
        amount += used_kwh * .035
    elif (used_kwh > 50 and used_kwh <= 150):
        amount += (((used_kwh - 50) * .45) + (50 * .35))
    elif (used_kwh > 150 and used_kwh <= 450):
        amount += (((used_kwh - 150) * .65) + (((150 - 50) * .45) + (50 * .35)))
    elif (used_kwh > 450 and used_kwh <= 2000):
        amount += (((used_kwh - 450) * .80) + ((450 - 150) * .65) + (((100 - 50) * .45) + (50 * .35)))
    else:
        print("Kilowatt Hours cannot be more than 2000!");
        exit()

    charge = "${:,.2f}".format(amount)
    print("Kilowatt-Hours used: ",used_kwh,", charge is: ",charge)

    count = count + 1

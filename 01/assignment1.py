#!/usr/bin/python

loan = int(input("Enter loan amount: "))
rate = float(input("Enter rate (4.5% entered as 0.045): "))
term = int(input("Enter term (in years): "))

# calculate mortgage
monthly_payment = ((loan * (rate / 12)) / 1 - (1 + rate / 12) **-12*term)

# round up
currency = "${:,.2f}".format(monthly_payment)
loan = "${:,.2f}".format(loan)

# rate = rate * 100
rate = "{:.2%}".format(rate)

print("A loan of",loan,"at an interest rate of",rate,"% for",term,"years is:",currency, "per month.")

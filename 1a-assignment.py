#!/usr/bin/python

loan = int(input("Enter loan amount: "))
rate = float(input("Enter rate (4.5% entered as 0.045): "))
term = int(input("Enter term (in years): "))

##monthly_payment = (amt_loan * (interest_rate / months)) / (1 - (1 + interest_rate / 12) **-months)
monthly_payment = ((loan * (rate / term)) / (1 - (1 + rate / 12) **-term*12))

#monthly_payment *= monthly_payment * term
currency = "${:,.2f}".format(monthly_payment)
loan = "${:,.2f}".format(loan)

#rate = rate * 100
rate = "{:.2%}".format(rate)

#loan * ((rate * ((1 + rate) ** term)) / ((1 + rate) ** term - 1))

print("A loan of",loan,"at an interest rate of",rate,"% for",term,"years is:",currency, "per month.")

# A loan of $600,000 at an interest rate of 0.045% for 30 years is $2345.67 per month.

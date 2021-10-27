#!/usr/bin/python

loan = int(input("Enter loan amount: "))
rate = float(input("Enter rate (4.5% entered as 0.045): "))
term = int(input("Enter term (in years): "))

#mortgage = 2123.45;

monthly_payment = loan * (rate/term)

print("A loan of",loan,"at an interest rate of",rate,"for",term,"years is:",monthly_payment,"per month.")

# A loan of $600,000 at an interest rate of 0.045% for 30 years is $2345.67 per month.

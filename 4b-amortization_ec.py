#/usr/bin/python
# File: 4b-amortization_ec
# Developer: Patrick Mims
# Date: 10.23.21
#
# This program uses a for loop 

amt_loan = int(input("Enter Loan Amount: "))
interest_rate = float(input("Enter interest rate: "))
months = int(input("Enter term in months: "))

loan = "{:.2f}".format(amt_loan)
rate = "{:.2f}".format(interest_rate)
term = "{:.1f}".format(months)

report = "Vehicle Loan Amortization Table"

ln = "Loan: "
ir = "Interest Rate: "
tm = "Term in months: "

col_1 = "Payment#"
col_2 = "Monthly"
col_3 = "Amount to"
col_4 = "Amount to"
col_5 = "Remaining"
col_6 = ""
col_7 = "Payment"
col_8 = "Interest"
col_9 = "Principal"
col_10 = "Balance"

print ("\n",report.rjust(39, ' '),"\n")
print (ln.rjust(15, ' '), "$", loan)
print (ir.rjust(24, ' '),rate,'%')
print (tm.rjust(25, ' '), term)
print ("\n")
print (col_1.rjust(17, ' '), col_2.rjust(17, ' '), col_3.rjust(24, ' '), col_4.rjust(25, ' '), col_5.rjust(20, ' '))
print (col_6.rjust(17, ' '), col_7.rjust(17, ' '), col_8.rjust(23, ' '), col_9.rjust(26, ' '), col_10.rjust(18, ' '))
print("\t____________________________________________________________________________________________________")
print ("\n")

count = 1

monthly_payment = (amt_loan * (interest_rate / months)) / (1 - (1 + interest_rate / 12) **-months) 

for count in range(months):
    interest_amount = (amt_loan * (interest_rate / months))
    amt_principal = (monthly_payment - interest_amount)
    remaining_balance = (amt_loan - amt_principal)

    if count < 10:
        print ("\t{0}{1:25.2f}{2:30.2f}{3:20.2f}{4:22.2f}".format(count, round(monthly_payment, 2), round(interest_amount, 2), round(amt_principal, 2), round(remaining_balance, 2)))
    else:
        print ("\t{0}{1:24.2f}{2:30.2f}{3:20.2f}{4:22.2f}".format(count, round(monthly_payment, 2), round(interest_amount, 2), round(amt_principal, 2), round(remaining_balance, 2)))

    count = count + 1

    amt_loan = remaining_balance 

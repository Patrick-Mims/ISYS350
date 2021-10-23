#/usr/bin/python

loan_amount = int(input("Enter Loan Amount: "))
interest_rate = float(input("Enter interest rate: "))
months = int(input("Enter term in months: "))

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

print (report.rjust(40, ' '), "\n")
print (ln.rjust(15, ' '))
print (ir.rjust(24, ' '))
print (tm.rjust(25, ' '))
print ("\n")
print (col_1.rjust(17, ' '), col_2.rjust(17, ' '), col_3.rjust(24, ' '), col_4.rjust(25, ' '), col_5.rjust(20, ' '))
print (col_6.rjust(17, ' '), col_7.rjust(17, ' '), col_8.rjust(23, ' '), col_9.rjust(26, ' '), col_10.rjust(18, ' '))
print("\t____________________________________________________________________________________________________")
print ("\n")

count = 0

while count < months:  
    monthly_payment = (loan_amount * (interest_rate / months)) / (1 - (1 + interest_rate / 12) **-months) 

    print ("\t{0}{1:25.2f}".format(count, round(monthly_payment, 2)))

    count = count + 1

    # The amount of interest column is calculated by multiplying the 
    # previous month's remaining balance by annual_rate / 12
#    interest_amount = loan_amount * (interest_rate / months)
#    principal_amount = monthly_payment - interest_amount
#    balance_remaining = loan_amount - principal_amount

#   loan_amount = monthly_payment - balance_remaining
#    print ("\t{0}{1:25.2f}{2:30.2f}{3:30.2f}{4:30.2f}".format(count, round(monthly_payment, 2), round(interest_amount, 2), round(principal_amount, 2), round(balance_remaining, 2)))
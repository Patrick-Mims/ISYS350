#!/usr/bin/python
# ISYS350, Section 2
# Patrick Mims
# Date: 10/20/21
# Professor: David Chao
# #

# ISYS 350, Fall 21, Assignment 3, Due Date: Wednesday, 10/6/21
# 
# Part 1
# 
# An Internet service provider offers three subscription packages to its customers, 
# plus a discount for nonprofit organizations:
#  
# Package A: 10 hours of access for $12.95 per month. Additional hours are $4.00 per hour.
# Package B: 20 hours of access for $14.95 per month. Additional hours are $2.00 per hour.
# Package C: Unlimited access for $35.95 per month.
# 
# A nonprofit organizations will get 20# discount on all packages.
# 
# Create a Python program that asks user to enter the following information:
#     The Package customer selects
#     The hours used
#     Is the customer a non-profit organization
# And compute the monthly charge accordingly.
#
# Input validation: The number of hours used in a month cannot exceed 744.�
# 
# Test your program with these data:
# a. Package A using 10 hours and is non-profit.
# b. Package B using 25 hours, not non-profit: cost: $24.95
# c. Package C using 800 hours, is non-profit: cost: input error
# 
# Enter package (A, B, C): a
# Enter hours used: 10
# Are you a non-profit organization?(y/n): y
# The service charge is: $10.36
# >>> 
# 
# Enter package (A, B, C): b
# Enter hours used: 25
# Are you a non-profit organization?(y/n): n
# The service charge is: $24.95
# >>> 
# 
# Enter package (A, B, C): c
# Enter hours used: 800
# Are you a non-profit organization?(y/n): y
# Hours cannot exceed 744!
# Note: Considering the possibility that user may enter the package with uppercase or lowercase letter, you may use string�s upper() or lower() to convert the package to the case you want in order to determine the package correctly in your program.
# 2 Extra Credits:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# Part 2
# An electric company charges customers based on Kilowatt-Hours (Kwh) used.� The rules to compute the charge are:
# 
# First 50 Kwh
# 35 cents per Kwh
# 
# Each of the next 100 Kwh (up to 150 Kwh), the first 50 Kwh used is still charged at 35 cents each
# 45 cents per Kwh
# 
# Each of the next 300 Kwh (up to 450 Kwh)
# 
# Kwhs used between 50 and 150 are charged at 45 cents each
# 65 cents per Kwh
# 
# All Kwh over 450,
# 
# Kwhs used between 150 and 450 are charged at 65 cents each
# 80 cents per KH
# 
# Create a Python program that asks a user to enter Kwh used, and compute the electricity charges.� The Kwh used could be a number with decimals.�
# 
# Requirements:
#     Input validation: Kilowatt-Hours cannot exceed 2000.�
#     Test your program with (1) Kwh=4500, (2) Kwh = 400
# 
# Turn in the program's screenshot and the code.
#
# ********* Sample run *********:
# 
# Enter Kilowatt-Hours used: 400
# Kilowatt-Hours used: 400.0 , charge is: $225.00
# 
# >>> 
# Enter Kilowatt-Hours used: 4500
# The Kilowatt-Hours used cannot be more than 2000!
# >>> 
# 
# Copy the source code and paste to a Word document, and copy the output and paste it to the same Word document. Submit the Word document by email attachment.

# #!/usr/bin/python
# 
# def calculate(choice, hours, n):
# 
#     service_charge = 0
#     discount_rate = .20
# 
#     # calculate discount
#     if choice == 'a':
#         base_rate = 12.95
#         base_hour = 10
# 
#         # check for discount
#         if n == 'y':
#             discount = base_rate * discount_rate 
#             message = "with a"
#         else:
#             discount = 0
#             message = "with out a"
# 
#         # check if hours are greater than 744
#         if hours >= 744:
#             print("Hours cannot exceed 744")
#             return
# 
#         # calculate additional hours 
#         if hours > base_hour:
#             additional_hours = hours - base_hour
#         else:
#             additional_hours = 0
# 
#         service_charge = (additional_hours * 4.00)
# 
#         total = service_charge + (base_rate - discount)
# 
#         print("\nTotal Package Deal: $",total,"per month",message,"$",discount,"discount\n")
# 
#     elif choice == 'b':
#         base_rate = 14.95
#         base_hour = 20
# 
#         if n == 'y':
#             discount = base_rate * discount_rate 
#             message = "with"
#         else:
#             discount = 0
#             message = "with out"
# 
#         # check if hours are greater than 744
#         if hours >= 744:
#             print("Hours cannot exceed 744")
#             return
# 
#         # calculate additional hours 
#         if hours > base_hour:
#             additional_hours = hours - base_hour
#         else:
#             additional_hours = 0
# 
#         # multiply the additional_hours by the extra $2.00
#         service_charge = (additional_hours * 2.00)
# 
#         # calculate the total
#         total = service_charge + (base_rate - discount)
# 
#         #print("The service charge for package", choice, "is", total, "per month")
#         print("\nTotal Package Deal: $"'{0:.2f}'.format(total),"per month",message,"a $",discount,"discount\n")
#     elif choice == 'c':
#         base_rate = 35.95
# 
#         if n == 'y':
#             discount = base_rate * discount_rate 
#             message = "with"
#         else:
#             discount = 0
#             message = "with out"
# 
#         # check if hours are greater than 744
#         if hours >= 744:
#             print("Hours cannot exceed 744")
#             return
# 
#         total = service_charge + (base_rate - discount)
# 
#         print("\nTotal Package Deal:",total,"per month",message,"a $",'{0:.2f}'.format(discount),"discount\n")
#     else: 
#         print("That's not an option")
# 
#     return
# 
# i = 1
# 
# # simple while loop 
# while i <= 6:
# 
#     pkg = input("\nEnter package (A, B, C): ") 
# 
#     if pkg == 'a' or pkg == 'b' or pkg == 'c':
#         hrs = int(input('Enter hours used: '))
#         isNonProfit = input("Are you a non-profit organization?(y/n): ")
#     else:
#         print("That's not an option!")
#         i += 1
# 
#     calculate(pkg, hrs, isNonProfit)
# 
#     i += 1

count = 0
service_charge = 0
additional_hours = 0
discount_rate = .20

while count <= 6:
    choice = input("\nEnter package (A, B, C): ") 

    if choice == 'a' or choice == 'b' or choice == 'c':

        hours = int(input('Enter hours used: '))

        if hours >= 744:
            print("Hours cannot exceed 744")
            break
        else: 
            charity = input("Are you a non-profit organization?(y/n): ")

            if charity == 'y':
                discount = 1
            else:
                discount = 0

            if choice == 'a':

                if discount:
                    discount = (12.95 * discount_rate) 
                    
                additional_hours = (hours - 10) 
                
                total = ((additional_hours * 4.00) + (12.95 - discount))

                print("\nThe service charge is: $", total)

            elif choice == 'b':
                print("\nPackage B: 20 hours of access for $14.95 per month. Additional hours are $2.00 per hour.")
            elif choice == 'c':
                print("\nPackage C: Unlimited access for $35.95 per month.")
            else:
                print("\nDone")
    else:
        print("That choice is not an option.")
        count = count + 1

#     # calculate discount
#     if choice == 'a':
#         base_rate = 12.95
#         base_hour = 10
# 
#         # check for discount
#         if n == 'y':
#             discount = base_rate * discount_rate 
#             message = "with a"
#         else:
#             discount = 0
#             message = "with out a"
# 
#         # check if hours are greater than 744
#         if hours >= 744:
#             print("Hours cannot exceed 744")
#             return
# 
#         # calculate additional hours 
#         if hours > base_hour:
#             additional_hours = hours - base_hour
#         else:
#             additional_hours = 0
# 
#         service_charge = (additional_hours * 4.00)
# 
#         total = service_charge + (base_rate - discount)
# 
#         print("\nTotal Package Deal: $",total,"per month",message,"$",discount,"discount\n")
# 
#     elif choice == 'b':
#         base_rate = 14.95
#         base_hour = 20
# 
#         if n == 'y':
#             discount = base_rate * discount_rate 
#             message = "with"
#         else:
#             discount = 0
#             message = "with out"
# 
#         # check if hours are greater than 744
#         if hours >= 744:
#             print("Hours cannot exceed 744")
#             return
# 
#         # calculate additional hours 
#         if hours > base_hour:
#             additional_hours = hours - base_hour
#         else:
#             additional_hours = 0
# 
#         # multiply the additional_hours by the extra $2.00
#         service_charge = (additional_hours * 2.00)
# 
#         # calculate the total
#         total = service_charge + (base_rate - discount)
# 
#         #print("The service charge for package", choice, "is", total, "per month")
#         print("\nTotal Package Deal: $"'{0:.2f}'.format(total),"per month",message,"a $",discount,"discount\n")
#     elif choice == 'c':
#         base_rate = 35.95
# 
#         if n == 'y':
#             discount = base_rate * discount_rate 
#             message = "with"
#         else:
#             discount = 0
#             message = "with out"
# 
#         # check if hours are greater than 744
#         if hours >= 744:
#             print("Hours cannot exceed 744")
#             return
# 
#         total = service_charge + (base_rate - discount)
# 
#         print("\nTotal Package Deal:",total,"per month",message,"a $",'{0:.2f}'.format(discount),"discount\n")
#     else: 
#         print("That's not an option")
# 
#     return
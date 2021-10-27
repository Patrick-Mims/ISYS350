#!/usr/bin/python
# ISYS350, Section 2
# Patrick Mims
# Date: 10/20/21
# Professor: David Chao
# #

additional_hours = 0
count = 0
discount_rate = .20
service_charge = 0

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
                if discount:
                    discount = (14.95 * discount_rate)

                    print("discount", discount)

                additional_hours = (hours - 20)

                total = ((additional_hours * 2.00) + (14.95 - discount))
                print("\nThe service charge is: $", total)
            elif choice == 'c':
                if discount:
                    discount = (34.95 * discount_rate)

                    print("\nThe service charge is: $", (34.95 - discount))
                    #print("\nPackage C: Unlimited access for $35.95 per month.")
                else:
                    print("\nDone")
            else:
                print("That choice is not an option.")
                count = count + 1

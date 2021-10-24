#!/usr/bin/python
# Patrick Mims
# Assignment 3A
# Class: ISYS-350 section 2
# Professor: David Chao
# Date: 10.20.21 
# #

additional_hours = 0
count = 0
discount_rate = .20

while count <= 3:
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
                
                print("\nThe service charge is: $", (((additional_hours * 4.00) + (12.95 - discount))))
            elif choice == 'b':
                if discount:
                    discount = (14.95 * discount_rate) 
                    
                additional_hours = (hours - 20) 
                
                print("\nThe service charge is: $", (((additional_hours * 2.00) + (14.95 - discount))))
            elif choice == 'c':
                if discount:
                    discount = (34.95 * discount_rate) 
                    
                print("\nThe service charge is: $", (34.95 - discount))
            else:
                print("\nDone")
    else:
        print("That choice is not an option.")
        count = count + 1
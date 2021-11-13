#!/usr/bin/python
# Name: Patrick Mims
# Assignment: 5 (Part 2)
# Date: November 11, 2021
# Professor: David Chao
# #

import module_employee as me

# create an empty array to hold the objects
employees = []

print("Sample Run\n")

# initialize the objects
employee1 = me.employee('Susan Meyers', '47899','Accounting', 'Vice President')
employee2 = me.employee('Mark Jones', '39119','IT', 'Programmer')
employee3 = me.employee('Joy Rogers', '81774','Manufacturing', 'Engineer')

# populate the array with the objects
employees.append(employee1)
employees.append(employee2)
employees.append(employee3)

# output the objects and properties 
for i in employees:
    print("Name: ", i.name)
    print("ID Number: ", i.id)
    print("Department: ", i.dept)
    print("Job Title: ", i.title, "\n")

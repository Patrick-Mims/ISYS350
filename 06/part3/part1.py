#!/usr/bin/python
# Name: Patrick Mims
# Assignment: 6 (Part 1)
# Date: November 10, 2021
# Professor: David Chao
# #

import datetime
import studentService as st

# create a new object
student = st.Student("S101", "Peter", "ISYS", "2019-08-20", 2.5)

print("\n")
# output objects and properties
print(student.studentID, " - ", student.studentName, " - ", student.major  , " - ", student.admittedDate, " - ", student.GPA)

# get academic status
student.academicStatus()

admitted_year = datetime.datetime.strptime(student.admittedDate, '%Y-%m-%d')
print("Estimated Time to Graduation:", student.estimatedGraduation(admitted_year));
print("\n")

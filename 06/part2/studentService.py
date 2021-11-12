#!/usr/bin/python
# Name: Patrick Mims
# Assignment: 6 Academic Status (Part 1)
# Date: November 11, 2021
# Professor: David Chao
# #

import datetime

class Student:
    def __init__(self, studentID, studentName, major, admittedDate, GPA):
        self.studentID = studentID
        self.studentName = studentName
        self.major = major
        self.admittedDate = admittedDate
        self.GPA = GPA

    def academicStatus(self):
        if self.GPA <= 2.0:
            print("Poor Academic Status")
        elif self.GPA <= 3.0:
            print("Fair academic status")
        else:
            print("Excellent Academic Status")

    def estimatedGraduation(self):
        admitted_year = datetime.datetime.strptime(self.admittedDate, '%Y-%m-%d')
        return admitted_year.year + 3 # 1095

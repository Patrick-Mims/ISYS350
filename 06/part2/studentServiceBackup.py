#!/usr/bin/python
# Name: Patrick Mims
# Assignment: 6 Academic Status (Part 2)
# Date: November 11, 2021
# Professor: David Chao
# #

print("Student Service");

class Student:
    def __init__(self, studentID, studentName, major, admitted, GPA):
        self.studentID = studentID
        self.studentName = studentName
        self.major = major
        self.admitted = admitted
        self.GPA = GPA

    def academicStatus(self, gpa):
        # if self.gpa < 2.0:
        if gpa < 2.0:
            print("Poor Academic Status")
        # elif self.gpa < 3.0:
        elif gpa < 3.0:
            print("Fair academic status")
        else:
            print("Excellent Academic Status")

    def estimatedGraduation(self, days):
        estimated_graduation_date = days
        return estimated_graduation_date

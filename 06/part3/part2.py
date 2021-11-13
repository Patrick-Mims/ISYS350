#!/usr/bin/python
# Name: Patrick Mims
# Assignment: 6 (Part 2)
# Date: November 10, 2021
# Professor: David Chao
# #

import csv
import datetime
import studentService as ss

header = [ 'StudentID', 'studentName', 'major', 'admittedDate', 'GPA' ]

student = [
    [ 'S101', 'Peter', 'ISYS', '2019-08-20', 2.5 ],
    [ 'S106', 'Paul', 'FIN', '2020-03-15', 3.0 ],
    [ 'S103', 'Mary', 'ISYS', '2020-05-15', 2.7 ]
]

# write the csv file
with open('student.csv', 'w', encoding='UTF8', newline='') as w:
    writer = csv.writer(w)

    # write header
    writer.writerow(header)

    # write rows
    writer.writerows(student)

# read the csv file
with open('student.csv', 'r', encoding='UTF8', newline='') as r:
    csv_reader = csv.reader(r)

    cnt = 0
    sum = 0

    # student print out and average GPA
    print("\n")
    print("ID\t Name\t Major\t Graduation\t GPA")
    for line in csv_reader:
        if cnt < 3:
            estimated_graduation = datetime.datetime.strptime(student[cnt][3], '%Y-%m-%d')
            print(student[cnt][0],"\t",student[cnt][1],"\t",student[cnt][2],"\t", (estimated_graduation.year + 3),"\t\t",student[cnt][4])
            sum = sum + student[cnt][4]
            cnt = cnt + 1

    print("\nTotal GPA : ", sum, "\n")

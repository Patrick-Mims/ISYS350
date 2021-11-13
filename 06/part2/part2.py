#!/usr/bin/python

import csv
import studentService as ss

header = [ 'StudentID', 'studentName', 'admittedDate', 'GPA' ]

student = [
    [ 'S101', 'Peter', 'ISYS', '2019-08-20', '2.5' ],
    [ 'S106', 'Paul', 'FIN', '2020-03-15', '3.0' ],
    [ 'S103', 'Mary', 'ISYS', '2020-05-15', '2.7' ]
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

    # print each line
    for line in csv_reader:
        print(line)

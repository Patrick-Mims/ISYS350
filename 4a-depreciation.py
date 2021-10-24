#!/usr/bin/python

count = 1

prop_value= int(input("Enter property value: "))
prop_life = int(input("Enter property life: "))

print("\n")
print("\tDouble Declining Depreciation Table\n")
print("\tProperty value: ", prop_value)
print("\tProperty life: ", prop_life,"\n")

year = "Year"
begin_year= "Value at"
during_year = "Depreciation"
total_depreciation = "Total depreciation"

empty = " "
b_year = "Begin Year" 
d_year = "During Year" 
e_year = "To End Year" 

print (year.rjust(12,' '), begin_year.rjust(17, ' '), during_year.rjust(24, ' '), total_depreciation.rjust(25, ' '))
print (empty.rjust(12,' '), b_year.rjust(19, ' '), d_year.rjust(21, ' '), e_year.rjust(19, ' '))
print("\t__________________________________________________________________________________________________________\n")

count = 0
depreciation = 0
total_depreciation = 0

while prop_life > count:
    count = count + 1
    depreciation = prop_value * 2 / prop_life
    total_depreciation = total_depreciation + depreciation
    print("\t{0}{1:20.2f}{2:20.2f}{3:20.2f}".format(count, round(prop_value, 2), round(depreciation, 2), round(total_depreciation, 2)))
    prop_value = prop_value - depreciation

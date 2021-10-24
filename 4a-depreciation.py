#!/usr/bin/python

count = 1

property_value = int(input("Enter property value: "))
property_life = int(input("Enter property life: "))

print("\n")
print("\tDouble Declining Depreciation Table\n")
print("\tProperty value: ", property_value)
print("\tProperty life: ", property_life,"\n")

year = "Year"
year_beginning = "Value at"
depriciationDuringYear = "Depreciation"
tp = "Total depreciation"

empty = " "
b_year = "Begin Year" 
d_year = "During Year" 
e_year = "To End Year" 

#print("\tYear\tDepreciation During the Year\tTotal depreciation to year end.")
print (year.rjust(12,' '), year_beginning.rjust(17, ' '), depriciationDuringYear.rjust(24, ' '), tp.rjust(25, ' '))
print (empty.rjust(12,' '), b_year.rjust(19, ' '), d_year.rjust(21, ' '), e_year.rjust(19, ' '))
print("\t__________________________________________________________________________________________________________\n")

count = 0
depreciation = 0
total_depreciation = 0

while property_life > count:
    count = count + 1
    depreciation = property_value * 2 / property_life
    total_depreciation = total_depreciation + depreciation
    print("\t{0}{1:20.2f}{2:20.2f}{3:20.2f}".format(count, round(property_value, 2), round(depreciation, 2), round(total_depreciation, 2)));
    property_value = property_value - depreciation

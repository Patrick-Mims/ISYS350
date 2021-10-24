#!/usr/bin/python

count = 1

prop_value = int(input("Enter property value: "))
prop_life = int(input("Enter property life: "))

pv = "{:.2f}".format(prop_value)
pf = "{:.1f}".format(prop_life)

print("\n")
print("\tDouble Declining Depreciation Table\n")
print("\tProperty value: $",pv)
print("\tProperty life: ", pf,"\n")

year = "Year"
begin_year= "Value at"
during_year = "Depreciation"
total_depreciation = "Total depreciation"

empty = " "
b_year = "Begin Year" 
d_year = "During Year" 
e_year = "To End Year" 

print (year.rjust(12,' '), begin_year.rjust(15, ' '), during_year.rjust(34, ' '), total_depreciation.rjust(25, ' '))
print (empty.rjust(12,' '), b_year.rjust(17, ' '), d_year.rjust(31, ' '), e_year.rjust(19, ' '))
print("\t__________________________________________________________________________________________________________\n")

count = 0
depreciation = 0
total_depreciation = 0

for count in range(prop_life):
    count = count + 1
    depreciation = prop_value * 2 / prop_life
    total_depreciation = total_depreciation + depreciation

    output_23 = "\t{0}{1:^30.2f}{2:^32.2f}{3:^1.2f}".format(count, round(prop_value, 2), round(depreciation, 2), round(total_depreciation, 2))
    output_20 = "\t{0}{1:^29.2f}{2:^32.2f}{3:^1.2f}".format(count, round(prop_value, 2), round(depreciation, 2), round(total_depreciation, 2))

    if(count < 10):
        print(output_23)
    else: 
        print(output_20)

    prop_value = prop_value - depreciation
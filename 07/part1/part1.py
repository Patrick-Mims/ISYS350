#!/usr/bin/python
# Name: Patrick Mims
# Assignment: 7 (Part 1)
# Date: November 18, 2021
# Professor: David Chao
# #

# necessary variables
check = 1
count = 0

# while loop for the phrase to search
while check != 0:
    phrase = input("Enter a search phrase: ") 
    answer = input("Would you like to enter another phrase? (Y/N) ")

    # I check for the answer being Y/y or N/n
    if((answer == 'N') or (answer == 'n')):
        # if the answer is n/N I then set the 
        # 'check' variable to 0 and exit the loop
        check = 0
    elif((answer == 'Y') or (answer == 'y')):
        check = 1
    else:
        check = 0

print("\n")

# while loop for the paragraph to search
while check != 1:
    paragraph = input("Enter a paragraph for analysis: ")
    _answer = input("Would you like to enter another paragraph? (Y/N) ")

    if((_answer == 'N') or (_answer == 'n')):
        check = 1
    elif((_answer == 'Y') or (_answer == 'y')):
        check = 0
    else:
        check = 1

paragraph_list = paragraph.split()

for item in paragraph_list: 
    if phrase.upper() in item.upper():
        count += 1

print(phrase,"appears",count,"times")

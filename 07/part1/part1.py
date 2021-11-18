#!/usr/bin/python

i = 0

phrase = input("Enter a search phrase: ") 

print("Text Phrase: ", phrase)

while i < 5:
    print("i > ", i)

    answer = input("Would you like to enter another phrase? (Y/N)")

    if(answer == 'N') or (answer == 'n'):
        print("No")
    elif(answer == 'Y') or (answer == 'y'):
        print("Yes")
    else:
        print("Try Again")

    i = i + 1

#   Part 1: 
#
#   Text Frequency Analysis 
#
#   Create a Python program that asks users to enter any number of texts
#   they are interested in analyzing and stores the texts in a list. 
#
#   A 'text' can be a word such as "like", or a phrase such as "I like it." Then, the 
#   program will ask users to enter paragraphs (you may copy from a news article), 
#   and for each text in the list, display either "Not Found" message if the text 
#   does not exist in the paragraphs; otherwise display the number of times the text 
#   is found. 
#
#   Hint: 
#   1. See examples on Slide # 18 to 24 of the Python Collections PowerPoint. 
#   2. You may use the "in" command and count method as explained on slide 18 and 19.
#
#   Do a case-insensitive search by applying string's lower() or upper() function to the search
#   texts and the search paragraphs. You may arrange code as below:

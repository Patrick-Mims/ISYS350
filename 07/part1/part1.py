#!/usr/bin/python

check = 1
count = 0

while check != 0:
    phrase = input("Enter a search phrase: ") 
    answer = input("Would you like to enter another phrase? (Y/N) ")

    if((answer == 'N') or (answer == 'n')):
        check = 0
    elif((answer == 'Y') or (answer == 'y')):
        check = 1
    else:
        check = 0

print("\n")

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
        

#for item in phraseList:
#
#        countWord = 0
#
#    if searchWord.upper() in paragraph.upper():
#        countWord = paragraph.upper().count(searchWord.upper())
#        print(str(countWord))
#
#for word in paragraph:
#
#print("Your paragraph: ", paragraph.count(phrase[i]))
#
#print(paragraph.count())
#
#if phrase in paragraph:
#   print("Yes, the phrase is in the paragraph")
#   found = True 
#else:
#   print("No it's not found")
#   found = False 
#
#
#if found:
#   phrase_count = phrase.count('S')
#   print(str(phrase_count))

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

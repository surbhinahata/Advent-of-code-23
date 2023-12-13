#!/usr/bin/env python3

# Data mining puzzle, in the file given below are strings with numbers and letters in it. Extract the first number and the last number, stick them together. At the end
# add all this two digit number together to get the sum 

import re

testfile = "/home/surbhin/Advent-of-code-23/day1/d1p1.txt"

with open (testfile, 'r') as fh:
    stringlist = [] #empty list to store all two digit number
    for line in fh:
        line = line.strip("\n") #stripping new line character
        line = re.findall(r'[^a-z]', line) #regex to find only digits '^' symbol means find opposite of something in this case opposite of alphabets
        firstdigit = line[0] #get the first digit in the regex list
        seconddigit = line[-1] #get the last digit in the regex list
        twodigit = int(str(firstdigit) + str(seconddigit)) #adding two strings together and converting into integer
        stringlist.append(twodigit) #initialized empty list and adding each two digit into the list
    #print(stringlist)
    sum_of_all_nums = sum(stringlist)
    print(sum_of_all_nums)

#54990 is the correct answer, which I got it right in the first try
        
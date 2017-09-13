'''
Course: MITx 6.00.1x Intro to Comp Sci
Date: 6 Sep 2017
Problem Set 1-2:
    Assume s is a string of lower case characters.

    Write a program that prints the number of times the string 'bob' occurs
    in s. For example, if s = 'azcbobobegghakl', then your program should 
    print:

    Number of times bob occurs is: 2
'''

#To test rebind variable s
s = 'oboobobobbobbbobbvbobboboboxbobobbtrboboboboboobobosobu'

count = 0
for l in s:
    if s[0:3] == 'bob':
       count += 1
    s = s[1:]
print('Number of times bob occurs is: ' + str(count))
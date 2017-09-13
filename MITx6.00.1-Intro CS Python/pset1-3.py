'''
Course: MITx 6.00.1x Intro to Comp Sci
Date: 7 Sep 2017
Problem Set 1-3:
    Assume s is a string of lower case characters.

    Write a program that prints the longest substring of s in which the 
    letters occur in alphabetical order. For example, if s = 'azcbobobegghakl',
    then your program should print:

    Longest substring in alphabetical order is: beggh

    In the case of ties, print the first substring. For example, 
    if s = 'abcbcd', then your program should print:

    Longest substring in alphabetical order is: abc
'''

#To test rebind variable s
s = 'jbuqaxpkqzcu'

test = ''     
longest = ''       
for n in range(0, len(s)):   
    if s[n] >= s[n-1]:
        test = test + s[n] 
    else:                    
        test = s[n]
    if len(test) > len(longest):
        longest = test
print("Longest substring in alphabetical order is: " + longest)

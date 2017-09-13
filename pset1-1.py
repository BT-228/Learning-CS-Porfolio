'''
Course: MITx 6.00.1x Intro to Comp Sci
Date: 6 Sep 2017
Problem Set 1-1:
    Assume s is a string of lower case characters.

    Write a program that counts up the number of vowels contained in the string s.
    Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if 
    s = 'azcbobobegghakl', your program should print:

    Number of vowels: 5
'''

#To test rebind variable s
s = 'ayhcmgkmitajhkkkarxw'

vowels = 0
for v in s:
    if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
        vowels += 1
print('Number of vowels: ' + str(vowels))
'''
Course: MITx 6.00.1x Intro to Comp Sci
Date: 14 Sep 2017
Problem Set 2-2:
    
    Now write a program that calculates the minimum fixed monthly payment 
    needed in order pay off a credit card balance within 12 months. By a 
    fixed monthly payment, we mean a single number which does not change 
    each month, but instead is a constant amount that will be paid each month.

    In this problem, we will not be dealing with a minimum monthly payment rate.

    The following variables contain values as described below:

        balance - the outstanding balance on the credit card

        annualInterestRate - annual interest rate as a decimal

    The program should print out one line: 
    the lowest monthly payment that will pay off all debt in under 1 year.
    
    Assume that the interest is compounded monthly according to the balance 
    at the end of the month (after the payment for that month is made). 
    The monthly payment must be a multiple of $10 and is the same for all 
    months. Notice that it is possible for the balance to become negative 
    using this payment scheme, which is okay.
'''

#variables with test values
balance = 3329
annualInterestRate = 0.2

#code to solve problem
mon_int_rate = annualInterestRate / 12.0
low_mpay = 0
rem_bal = balance

while rem_bal > 0:
    months = 12
    while months > 0:
        rem_bal = (rem_bal - low_mpay)*(1+(mon_int_rate))
        months -= 1
    if rem_bal > 0:
        low_mpay += 10
        rem_bal = balance
        months += 12
else:
    print('Lowest payment: ' + str(round(low_mpay, 2)))
    
    
    


















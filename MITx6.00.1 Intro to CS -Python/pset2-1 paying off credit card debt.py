'''
Course: MITx 6.00.1x Intro to Comp Sci
Date: 13 Sep 2017
Problem Set 2-1:
    
    Write a program to calculate the credit card balance after one year if 
    a person only pays the minimum monthly payment required by the credit card 
    company each month.

    The following variables contain values as described below:

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

    monthlyPaymentRate - minimum monthly payment rate as a decimal
    
    For each month, calculate statements on the monthly payment and remaining 
    balance. At the end of 12 months, print out the remaining balance. Be sure 
    to print out no more than two decimal digits of accuracy. 
'''

#variables with test values
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#code to solve problem.
#solution did not require a function and rather a while loop was sufficient.
def remainbal(balance, annualInterestRate, monthlyPaymentRate):
    '''
    Function returns the remaining balance of a credit card after one year 
    with the following parameters:
        
        balance = initial amount
        annualInterestRate = annual interest rate as a decimal
        monthlyPaymentRate = monthly payment rate as a decimal
    '''
    months = 12
    new_bal = balance
    while months > 0:
        new_bal = (new_bal - (new_bal*monthlyPaymentRate))*(1+(annualInterestRate/12))
        months -= 1
    return 'Remaining balance: ' + str(round(new_bal, 2))
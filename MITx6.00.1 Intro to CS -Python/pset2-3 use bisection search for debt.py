'''
Course: MITx 6.00.1x Intro to Comp Sci
Date: 15 Sep 2017
Problem Set 2-3:
    
    ...how can we calculate a more accurate fixed monthly 
    payment than we did in Problem 2 without running into the problem of 
    slow code? We can make this program run faster using a technique 
    introduced in lecture - bisection search!

    The following variables contain values as described below:

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal
    
    To recap the problem: we are searching for the smallest monthly 
    payment such that we can pay off the entire balance within a year. 
    What is a reasonable lower bound for this payment value? $0 is the 
    obvious anwer, but you can do better than that. If there was no 
    interest, the debt can be paid off by monthly payments of one-twelfth 
    of the original balance, so we must pay at least this much every month. 
    One-twelfth of the original balance is a good lower bound.

    What is a good upper bound? Imagine that instead of paying monthly, 
    we paid off the entire balance at the end of the year. What we ultimately 
    pay must be greater than what we would've paid in monthly installments, 
    because the interest was compounded on the balance we didn't pay off each 
    month. So a good upper bound for the monthly payment would be one-twelfth 
    of the balance, after having its interest compounded monthly for an entire 
    year.
    
    Write a program that uses these bounds and bisection search  
    to find the smallest monthly payment to the cent (no more multiples 
    of $10) such that we can pay off the debt within a year. Try it out 
    with large inputs, and notice how fast it is (try the same large inputs 
    in your solution to Problem 2 to compare!). Produce the same return value 
    as you did in Problem 2.
'''

#variables with test values
balance = 320000
annualInterestRate = 0.2

#code to solve problem
mon_int = annualInterestRate / 12.0
low = balance / 12.0
high = (balance*(1+mon_int)**12) / 12.0

mpay = (high + low) / 2.0
epsilon = 0.01
rem_bal = balance
months = 12

while rem_bal != epsilon:
    while months > 0:
        rem_bal = (rem_bal - mpay)*(1+(mon_int))
        months -= 1
    if round(rem_bal,2) > epsilon:
        low = mpay
    if round(rem_bal,2) < epsilon:
        high = mpay
    if round(rem_bal,2) == epsilon:
        print('Lowest Payment: ' + str(round(mpay, 2)))
        break
    mpay = (high + low) / 2.0
    months += 12
    rem_bal = balance












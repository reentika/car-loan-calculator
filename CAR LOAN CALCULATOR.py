# -*- coding: utf-8 -*-
"""
Reentika Awasthi
11/9/2021
To tell the user the monthly payment, interest rate and the amount paid through the whole mortgage, total payments, based on information entered by them

"""

file = open("cars.csv")


header = file.readline()


# tax is 12%
cost = float(input("Vehicle cost ($): "))
interest = float(input("Annual interest rate (%): "))/100
duration = int(input("Duration of loan (years): "))


loan_amount = cost * 0.12 + cost # cost with tax :) also is the principal

original_loan_amount = loan_amount
monthly_interest = interest / 12

months = duration*12

# shorten variables to calculate easily. 
p = loan_amount
r = monthly_interest
n = months

A = p * (r*(1 +r)**n) 
B = (1 + r)**n- 1
monthly_payment = A/B
monthly_payment = monthly_payment



print("Monthly payment: {:.2f}" .format(monthly_payment))

payments = 0
interest_paid = 0
balance = loan_amount
time = 1 

while time != duration + 1:
    for year in range (12):
        interest_portion = loan_amount * interest / 12
        toward_principal = monthly_payment - interest_portion 
        balance = loan_amount - toward_principal 
        loan_amount = balance
        if year == 11:
            print("Year " + str(time) + " balance: {:.2f}".format(loan_amount))
            time += 1 
        payments += monthly_payment
        interest_paid += interest_portion
 
         

print("Loan amount: {:.2f}" .format(original_loan_amount))
print("Monthly paymemt: {:.2f} ".format(monthly_payment))
interest_rate = interest*100
print("Interest rate: {:.2f} " .format(interest_rate) +"%")
print ("Total payments: {:.2f} ".format(payments))
print("Interest paid: {:.2f}".format(interest_paid))




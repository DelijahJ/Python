# Author:         Delijah Joseph
# Major:          Information Technology
# Creation Date:  January 31, 2022
# Due Date:       February 11, 2022
# Course:         CSC223
# Professor Name: Professor Earl 
# Assignment:     #1
# Filename:       hw1_payroll.py
# Purpose:        Solve a problem using the Python programming language, Demonstrate the ability to declare variables and use control structures in Python

done = 0
while done == 0:
    print("This is a program to process employee pay")

    print("Enter Your Name:")
    name = str(input()) 
    if name == 'done':
        done = 1
        break
    totalHrs = 0

    print("Enter your hourly rate")
    wage = float(input())
    if wage < 0:
        print("You cannot earn less then 0 dollars!")
        done = 1
        break

    num = 1
    while (num < 6):
        print("Enter number of hours worked for day: " + str(num)) 
        hours = float(input())
        if hours < 0:
            print("You cant work less then 0 hours!")
            continue

        if hours > 24:
            print("You cant work more then 24 hours!")
            continue
        num = num + 1
        totalHrs = totalHrs + hours

    federal = 0
    grossPay = totalHrs * wage
    stateTax = grossPay * .0307
    fica = grossPay * .0886
    if grossPay < 5000:
        federal = grossPay * .15
    else: federal = grossPay * .25
    withholdings = stateTax + fica + federal
    netPay = grossPay - withholdings
    print(name)
    print("Gross Pay:" , "${:.2f}".format(grossPay))
    print("Total Withholding amount:", "${:.2f}".format(withholdings))
    print("Net Pay:" , "${:.2f}".format(netPay))
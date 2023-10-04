print("Enter Your Name:")
name = str(input()) 
print("Enter number of hours worked:")
hours = int(input())
wage = int(input("Enter your hourly rate:"))

if hours < 0:
    print("You cant work less then 0 hours!")

elif wage < 0:
    print()
    pay = hours * wage 
    print("Payment Amount: $" + str(pay))
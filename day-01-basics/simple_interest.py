# Question 10: Write a Python program to calculate simple interest.
num1 = float(input("Enter the principal amount: "))
num2 = float(input("Enter the rate of interest (in %): "))
num3 = float(input("Enter the time period (in years): "))
simple_interest = (num1 * num2 * num3) / 100
print("The simple interest is:", simple_interest)
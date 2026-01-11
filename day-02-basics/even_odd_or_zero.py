# Day 2 Question 1: Write a Python program to determine if a number is even, odd, or zero
num1 = int(input("Enter a Integer: "))
if num1 == 0:
    print("The number is zero.")
elif num1 % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


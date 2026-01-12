# Day 3 Question 4 : Write a Python program to Take a number as input and print its multiplication table from 1 to 10 and print it.
# Login : Using for loop to execute block of code multiple times to multiply the number with each number from 1 to 10 and print it.
num = int(input("Enter a Integer:"))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)

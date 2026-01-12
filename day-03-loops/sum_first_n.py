# Day 3 Question 3 : Write a Python program to take N as input and print the sum of numbers from 1 to N. 
# Login : Using a for Loop to execute block of code to add each number from1 to N and print its sum.
n = int(input("Enter a Integer N: "))
sum = 0
for i in range(1, n+1):
    sum +=i
print("The sum of numbers from 1 to", n,"is:",sum)

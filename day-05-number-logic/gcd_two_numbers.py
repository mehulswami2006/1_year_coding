# Day 5 Question 4 : Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.
# Logic : The GCD of two numbers is the largest number that divides both of them without leaving a remainder. Python has a direct keyword to fing GCD in math module, but we will use logic.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = 1# since all numbers are divisible by 1
for i in range(1, min(num1, num2) + 1):# will check for i from 1 to minimum of num1 and num2(+1 is because range will stop just before the end number give in range parameter)
    if (num1 % i == 0) and (num2 % i == 0):# 1st check if i divides num1 then for num2 
        gcd = i# if true gcd becomes i
print("The GCD of", num1, "and", num2, "is", gcd)# print final gcd
# Process: Example num1=20 & num2=30
# i=1 divides 20 & 30 gcd=1
# i=2 divides 20 & 30 gcd=2
# i=3 does not divide 20 gcd=2
# i=4 divides 20 but not 30 gcd=2
# i=5 divides 20 & 30 gcd=5
# i=6 does not divide 20 gcd=5
# i=7 does not divide 20 gcd=5
# i=8 does not divide 20 gcd=5
# i=9 does not divide 20 gcd=5
# i=10 divides 20 & 30 gcd=10
# ... so on till i=20 (minimum of 20 and 30)
# Final GCD=10
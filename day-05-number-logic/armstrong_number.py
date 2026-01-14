# Day 5 Question 1 : Write a Python program to check whether a number is armstrong or not.
# Logic : An Armstrong number for a three-digit number is a number that is equal to the sum of the cubes of its digits.
num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

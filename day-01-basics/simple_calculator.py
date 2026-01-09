# Question 6: Write a Python program to take 2 integers and print Sum, Difference, Product and Division.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
sum = num1 + num2
difference =num1 - num2
product = num1 * num2
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
if num1 == 0 or num2 == 0:
    print("Division: Undefined")
else: 
    division = num1 / num2
    print("Division:", division)



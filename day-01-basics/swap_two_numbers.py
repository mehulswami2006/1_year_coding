# Question 9: Write a Python program to swap two numbers using a temporary variable.
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
print("Before swapping:")
print("a =", a)
print("b =", b)
temp = a
a = b
b = temp
print("After swapping:")
print("a =", a)
print("b =", b)
# Day 5 Question 1 : Write a Python program to check whether a number is prime or not.
# Logic : A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. Therefore, checking if the number is divisible only by 1 and itself.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print("Invalid!! Enter a number greater than 1")
# Day 5 Question 2 : Write a Python program to print all prime numbers from 1 to n.
# Logic : A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. Therefore, checking if each number in the range is divisible only by 1 and itself.
n = int(input("Enter a number: "))   
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
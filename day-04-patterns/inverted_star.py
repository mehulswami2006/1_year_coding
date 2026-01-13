# Day 4 Question 2 : Write a Python program to print inverted Right-Angles star pattern.
# Logic : Using Loop inside another loop to print inverted Right-Angles star pattern.
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
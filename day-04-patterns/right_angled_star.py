# Day 4 Question 1 : Write a Python program to print right angled star pattern.
# Logic : Using Loop inside another loop to print right angless star pattern.
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()
    
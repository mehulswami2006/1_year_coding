# Day 4 Question 4 : Write a Python program to print square pattern.
# Logic : Using Loop inside another loop to print square pattern.  
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(rows):
        print("*", end="")
    print()
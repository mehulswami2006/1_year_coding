# Day 4 Question 3 : Write a Python program to print number pattern.
# Logic : using loop inside another loop to print numbe pattern.
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
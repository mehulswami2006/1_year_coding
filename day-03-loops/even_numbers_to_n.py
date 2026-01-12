# Day 3 Question 2 : Write a Python program to print even numbers from 1 to N using loops.
# Logic : Using a for Loop to execute block of code to check each number between 1 to N foe even number and print it if even also number of even numberss.
n = int(input("Enter a integer N: "))
count = 0
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
        count += 1
print("Total even number from 1 to", n,"is:",count)
# Day 3 Question 5 : Write a Python pogram to take a number and print how many digits it has.
#Logic : Using while loop to execute block of code multiple time to divide the number by 10 until it become 0 and count the number of times the Loop runs to get the number of digits.
num = int(input("Enter a Integer: "))
count = 0
while num >0:
    num = num //10
    count +=1
print("The number of digits is:",count)
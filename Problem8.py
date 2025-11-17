# Write a Python Program to print the factor of a number

n = int(input("Enter the Number:"))

for i in range(1,n+1):
    if n%i == 0:
        print(i)
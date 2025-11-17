# Write a Python Program to accept a number and check it is perfect number or not.

n = int(input("enter the The number:"))
sum = 0

for i in range(1,n):
    if n%i == 0:
       sum = sum+i
if sum == n:
    print("The number is perfect Number")
else:
    print("The number is not perfect number")

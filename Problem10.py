# Write a Python Program to print the Prime number 1 to 20

n = int(input("Enter the number where till you want:"))
count = 0
for i in range(1,n+1):
    if n%i == 0:
        print(i)
        count = count + 1
if count == 2:
    print("Number is prime")
else:
    print("Number is not prime")

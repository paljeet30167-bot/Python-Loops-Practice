# Write a Python program to print he sumo f n numbers

n = int(input("Enter your Number:"))
sum = 0

for i in range(1,n+1):
    sum = sum + i
print(f"Your sum is {sum}")
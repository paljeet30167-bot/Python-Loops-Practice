# Write a prpgram to take a input form the user and Print the table of the any number using for loop 
n = int(input("Enter your number you want :"))
for i in range(1,11):
    print(f"{n}*{i} = {n*i}")


n = int(input("Enter your number you want :"))
for i in range(n,(n*10)+1,n):
    print(i)
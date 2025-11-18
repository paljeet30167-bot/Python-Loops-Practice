# Check a String is Pallindrome or not.

x = "NAMAN"
b = ""
for i in range(len(x)-1,-1,-1):
    print(x[i])
    b = b + x[i]
print(b)
if b == x:
    print("The string is palindrome")
else:
    print("It is not plaindrom:")
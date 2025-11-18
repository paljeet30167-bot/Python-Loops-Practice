# Count all letter ,digitd, special symbols, from any string you want

a = "jeet123@$%"

digits = 0
char = 0
symb = 0

for i in a:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        char += 1
    else:
        symb += 1
print(f"your digits are:{digits}\nYour characters are: {char}\n Your symbol are:{symb}")
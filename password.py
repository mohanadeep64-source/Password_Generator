import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!','#','$','%','&','(',')','*','+']
print("welcome to password generator")
a = int(input("enter number of letters"))
b = int(input("enter number of numbers"))
c = int(input("enter number of symbols"))
password_lst = []
for i in range(1,a+1):
    char = random.choice(letters)
    password_lst += char
for i in range(1,b+1):
    char=random.choice(symbols)
    password_lst += char
for i in range(1,c+1):
    char=random.choice(numbers)
    password_lst += char
print((password_lst))
random.shuffle(password_lst)
pass1 = ""
for i in password_lst:
    pass1 += i
print(pass1)

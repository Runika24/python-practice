print("hello world")
a=88
b=33
print(a+b)
print(a-b)
print(a*b)
print(a/b)
str="my name is Runika"
print(str)
print(str.lower())
print(str.upper())
print(str.replace("Runika","RUNIKA"))
print(type(str))
print(len(str))
print(type(a))
print(str[11])
print(str[1::2])
print(str[-1:-10:-2])
print(id(a))
num1=1+2j
num2=2+3j
print(type(num1))
print(type(num2))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1**num2)

set1={1,2,3,4}
set2={1,2,3,4,5,11,33,55}
print(set2.union(set1))



# conditional statements-->if and else statements,elif
# if and else statements

num0=0
if num1==0:
    print("zero")
else:
    print("not zero")

#elif(ladder if statement)

a1 = 1
if a1>1: 
    print("positive")
elif a1 == 0 :
    print("zero")
elif a1 == 1:
    print("one")
elif a1 == -1:
    print("-1")
elif a1 == -2:
    print("-2")
elif a1 == 1:
    print("one")
else:
    print("negative")

#loops-while,for

for i in range(0,15):
    if i % 2 == 0:
        print(i, "is an even number")
    else:
        print(i, "is an odd number")

num = 5
while num < 26:
    if num % 2 == 0:
        print(num,"Even")
    else:
        print(num,"Odd")
    num += 1

 # Jump statements-->break, continue

for i in range(0,8):
    print(i)
    if i == 5:
        break

for i in range(0,8):
    if i == 3: 
        continue
    print(i)

#Write a Python program to generate a random number.
    
import random
print(f"Random number: {random.randint(1, 100)}")
print("random number:",random.randint(1,1000))

#Write a Python program to display calendar.

import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year, month)
print(cal)

#prime number
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
            return True
print(is_prime(33))

#negative_number
# def negative_number():
#     while n>= 0:
#         n = int(input("enter a number:"))
#         print(negative_number(n))

# def negative_number(n):
#     n = int(input("enter a number:"))
#     while n>= 0:
#         negative_number()
# print(negative_number())
def negative_number():
    while True:
        n = int(input("Enter a number: "))
        if n < 0:
            print("You entered a negative number.")
            break

print(negative_number())
##while True: is used when you want to create an infinite loop—that is, a loop that runs forever unless you explicitly break out of it.
#If you don’t include a break, or some other way to exit the loop (like return or sys.exit()), the program will run forever.

# ----------faonucci series------------
# 
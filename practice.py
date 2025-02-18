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

list1=[1,2,6,7,9,00,66,"abc"]
tuple1=(1,2,6,7,9,00,66,55,11,"abc")

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

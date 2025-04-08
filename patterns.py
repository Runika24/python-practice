n=5
for i in range(n):
    for j in range(n):
        if i <=j:
            print("*",end =" ")
        else:
            print(" ",end = " ")
    print()    

print("--------------------------------------------------------------")

for i in range(n):
    for j in range(n):
        if i == 0 or j== 0 or j == n-1 or i == n-1:
            print("*",end = "  ")
        else:
            print(" ",end= "  ")
    print()  

print("--------------------------------------------------------------")

for i in range(n):
    for j in range(n):
        if i >= j :
            print("*",end = " ")
        else:
            print(" ",end =" ")
    print()        

print("--------------------------------------------------------------")
n=9
for i in range(n):
    for j in range(n):
        if i == 0 or i== n-1 or i + j == n-1 or i == j:
            print("*",end = "  ")
        else:
            print(" ",end= "  ")
    print()  

print("-------------------------------------------------------------") 

n=9
for i in range(n):
    for j in range(n):
        if j == 0 or j== n-1 or i + j == n-1 or i == j:
            print("*",end = "  ")
        else:
            print(" ",end= "  ")
    print()  

print("-------------------------------------------------------------------")
n=9
for i in range(n):
    for j in range(n):
        if i == 0 or i== n-1 or i + j == n-1 or i == j or j ==0 or j ==n-1:
            print("*",end = "  ")
        else:
            print(" ",end= "  ")
    print()      

print("-------------------------------------------------------------------")
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or i==j :
            print("*",end = "  ")
        else:
            print(" ",end= "  ")
    print()  

print("-------------------------------------------------------------------")
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i==j :
            print("*",end = "  ")
        else:
            print(" ",end= "  ")
    print()     

print("-------------------------------------------------------------------")
n=5
for i in range(n):
    for j in range(n):
        if i>=j :
            print("*",end = "  ")
        else:
            print(" ",end= "  ")
    print()  

for i in range(n):
    for j in range(n):
        if i<=j:
             print("*",end = "  ")
        else:
            print(" ",end= "  ")        
    print()
print("---------------------------------------------------------------------")
# for i in range(n):
#     for j in range(n):
#         if i>=j :
#             print("*",end = "  ")
#         else:
#             print(" ",end= "  ")
#     print()  

# for i in range(n):
#     for j in range(n):
#         if j==i and j <=n-1:
#              print("*",end = "  ")
#         else:
#             print(" ",end= "  ")        
#     print()    


n=1
for i in range(0,5):
    for j in range(n):
        if i>=j :
            print(n,end = "  ")
            n += 1
        else:
            print(" ",end= "  ")
    print()  

n=1
for i in range(0,5):
    for j in range(n):
        if i==j or j ==0 or i ==n-1:
            print(n,end = "  ")
            n += 1
        else:
            print(" ",end= "  ")
    print()  


print("-----------------------------------------")

for i in range(0,5):
    n=1
    for j in range(5):
        print(n,end = "  ")
        n += 1
    print()  

print("-----------------------------------------")
print(chr(82))
print(chr(65))

print(ord("a"))
print("a")


print("-----------------------------------------")

chr_num =65
for i in range(0,5):
    
    for j in range(5):
        print(chr(chr_num),end = "  ")
        chr_num += 1
    print()  

print("-----------------------------------------")
chr_num =65
for i in range(0,5):
    
    for j in range(5):
        if i<= j:
            print(chr(chr_num),end = "  ")
            chr_num += 1
        else:
            print(" ",end = "  ")    
    print()  
print("-----------------------------------------")

chr_num =65
for i in range(0,5):  
    for j in range(5):
        if i>= j:
            print(chr(chr_num),end = "  ")
            chr_num += 1
        else:
            print(" ",end = "  ")    
    print()  

print("-----------------------------------------")

# multiple inputs at a time............................
num1 ,num2 ,num3 = input("enter 3 numbers:").split(",")
print(num1,num2,num3)




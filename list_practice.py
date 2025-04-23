
#sorting based on length of strings
a =["aaa","aaaa","aaa","aa","a"]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if len(a[i])-1 > len(a[j])-1:
            a[i],a[j] = a[j],a[i]
print(a)

#################################

list=[1,2,3,4,5,6,7,88,1,1,1,23,3,4]
new_list=[]
for i in list:
    if i not in new_list:
        new_list +=[i]  #appending without .append()method
print(new_list)

############################
str ='python developer'
for x in str:
    if x not in 'aeiouAEIOU':
        print(x, end=" ")
print()

################

list1 = [0,1,2,3,4,5,6]
for i in range(len(list1)):
    if list1[i]%2 == 0:
        list1[i]=list1[i]*5
print(list1)

######################
# multiply integers and float with 2
li = [10,1.32,'python',True,20]
for i in range(len(li)-1):
    if type(li[i])==int or type(li[i])==float:
        li[i]=li[i]*2   
print(li)

###### printing alphabets#################################

count=65
for i in range(26):
    print(chr(count),end="  ")
    count +=1       
print()
#.......counting number of vovels in a string .............
str1 ='python developer'
count =0
for i in range(len(str1)):
    if str1[i] in 'aeiouAEIOU':
        count +=1  
print(count)        

####.....methods in lists.....................
k=[1,2,3,4,5,6,8,9,10]
k.append(100) ##add a element to the last of the list
k.insert(0,20) ## add a element at a specific index
k.sort(reverse=True) #print a list in decending order
k.pop(2)# delete the element
k.sort()# print a list in ascending order
print(len(k))
print(max(k))
print(min(k))
print(k)


### finding length of string without len()method
def u_length(p):
    count=0
    for i in p:
        count+=1
    print(count)
u_length('python')    

## Print all the Armstrong numbers in given range
num1 = int(input("enter a number :"));
temp = num1;
sum = 0;
n = len(str(num1))
while temp > 0:
   rem = temp % 10
   pow = rem**n;
   sum += pow
   temp //= 10
if (sum == num1):
      print(num1 , "Armstrong Number")
else:
      print(num1 , "not an ARMSTRONG NUMBER")

#

class Bank:
    def __init__(self,name,A_no):
        self.name = name
        self.A_no =A_no
        self.Balance = 10000
    def Deposit(self,a_no,money):
        self.a_no = a_no
        self.money = money
        if self.A_no == self.a_no:
            print("current balance :", self.Balance +self.money) 

obj=Bank('Runika',200200202)
obj.Deposit(200200202,10000000000)

class Bank:
    def __init__(self,name,A_no):
        self.name = name
        self.A_no =A_no
        self.Balance = 20000
    def Deposit(self,a_no,money):
        self.a_no = a_no
        self.money = money
        if self.A_no == self.a_no:
            print("current balance :", self.Balance +self.money) 
    def Withdraw(self,a_no,amount):
        self.a_no = a_no
        self.amount = amount    
        if self.A_no == self.a_no and self.Balance >= self.amount:
            print("current balance :" , self.Balance -  self.amount)
        if self.Balance < self.amount:
            print("insufficient balance")
            print("current balance :" ,self.Balance)
obj=Bank('Runika',200200202)
obj.Withdraw(200200202,20001)


# p=[1,2,3,4,5,6,7,8]
# p=[1,{2,3},{4,5},{6,7,8}]


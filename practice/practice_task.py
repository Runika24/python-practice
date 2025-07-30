


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


# print("-----------------amstrong number-------------------------------")

# num1 = int(input("enter a number :"));
# temp = num1;
# sum = 0;
# n = len(str(num1))
# while temp > 0:
#    rem = temp % 10
#    pow = rem**n;
#    sum += pow
#    temp //= 10
# if (sum == num1):
#       print(num1 , "Armstrong Number")
# else:
#       print(num1 , "not an ARMSTRONG NUMBER")

# print("-----------convertion of cases-------------------------------")  

# str = input("enter a string :")  ##Hello World
# str1 = ""
# for char in str:
#     if char.islower():
#         str1 += char.upper()
#     elif char.isupper():
#         str1 += char.lower()
#     else:
#         str1 += char       
# print(str1)


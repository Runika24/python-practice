# factorial-------------
# def factorial(num):
#     if not isinstance(num,int):
#         return None
#     if num < 0 :
#         return None
#     if num == 0 :
#         return 1
#     i =0
#     f=1
#     while i < num :
#         i  = i+1
#         f = f *i
#     return f
# print(factorial(5)) 

# fibonacci series of a range of numbers-------------
# def fibonacci(n):
#     if not isinstance(n,int):
#         return None
#     elif n <= 0 :
#         return 0
#     elif  n==1 :
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# for i in range(10):
#     print(fibonacci(i) ,end=" ")


## method 2
# def fibanocci(n):
#     a,b = 0,1
#     for _ in range(n):
#         print(a,end=" ")
#         a,b = b,a+b
# print(fibanocci(10))

#  Ask the user to enter a word and check if it is a palindrome (reads the same backward and forward).
# Input: "madam"
# Output: "It is a palindrome."

#using slicing-----------------------------------
# def check_palindrome(input_str):
#     if input_str == input_str[::-1]:
#         return "it is a palindrome"
#     else:
#         return "not a palindrome"
# print(check_palindrome("madam"))

##using loops--------------
# def check_palindrome(input_str): 
#     str = input_str.lower()   
#     low = 0
#     high = len(str) -1
#     for i in range (len(str)-1):
#         if str[low] != str[high]:
#             return False
#         low +=1
#         high -= 1
#         return True
# print(check_palindrome("Madam"))


##strong number---------
# def fact (a):
#     s =1
#     for i in range(1,a+1):
#         s = s*i
#     return s
# def is_strong(n):
#     t=n
#     total =0
#     while t >0:
#         a = t % 10
#         total =total+fact(a)
#         t//=10
#     return total == n   
# print(is_strong(145))


#Reverse a String
# def rev_str(input_str):
#     str = ""
#     low =0
#     high =len(input_str)-1
#     for i in range (0,len(input_str)):
#         str+=input_str[high]
#         high-=1
#     return str    
# print(rev_str("RUNIKA"))        

#Count Vowels and Consonants in a String
# input_str = "Runika.koosa  ".lower()
# vowel = 0
# space = 0
# consonent = 0
# other = 0
# for i in input_str:
#     if i in 'aeiou':
#         vowel += 1
#     elif i.isalpha():
#         consonent += 1
#     elif i == ' ':
#         space += 1
#     else:
#         other += 1
    
# print(vowel)  
# print(consonent)
# print(space)
# print(other) 


#Find Max/Min in a List Without max()/min()
# li = [1,2,9,-9,7,0,3,2,2,2,1,100]
# if len(li) > 0:
#     max = li[0]
#     min = li[0]
#     for i in li:
#         if i > max:
#             max = i
#     for i in li:
#         if min > i:
#             min = i              
# print(max)
# print(min)

#Sum of Digits of a Number


# def sum_digit(num):
#     temp = num
#     sum =0
#     while temp >0 :
#         digit = temp %10
#         temp //= 10
#         sum += digit
#     return sum
# print(sum_digit(2345)) 
# 
#    
#Check if Number is Prime
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2,num//2):
#         if num %i ==0:
#             return False
#     return True
# print(is_prime(23))  


# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2,num//2):
#         if num %i ==0:
#             return False
#     return num
# for i in range(1,101):
#     if is_prime(i):
#         print(i,end=" ")

#Find the Second Largest Number in a List

# li =[1,2,6,7,88,889,8891]
# li_new = []
# max = li[0]
# for i in li:
#     i> max
#     max = i 
#     li_new.append(max)
# print(max)    


# list1 = [1,1,2,3,4,55,55,6,7,12,88,76,99,1,2,333,4,555]
# visited_list = []
# output_list = set() #=> set doesn't allow duplicates
# for i in list1:
#     if i in visited_list:
#         print(i,"is duplicate list") 
#         output_list.add(i)  
#     else:
#         visited_list.append(i)
# print(visited_list)
# print(output_list) 

# i = 0
# while i < 3: 
# 	print(i) 
# 	i += 1
# else: 
# 	print(0)

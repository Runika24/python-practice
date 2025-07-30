
# #finding number of characters present in every string....

# str = 'full stack python developer'
# str2 = str.split(" ")
# print(str2)
# count =0
# arr = []
# for i in range(len(str2)):
#     for j in range(len(str2[i])):
#         count += 1  
#     arr.append(count)
#     count =0 
# print(arr)      

# #.......converting integer into string...............................

# # j = 1234
# # input_int = '0123456789'
# # res = ""
# # while j > 0 :
# #     digit =j %10
# #     j = j // 10 
# #     for i in range (len(input_int)):
# #         if digit == i :
# #             res = input_int[i] + res
# # print(res)
# # print(type(res))         

# #.......converting string into integer...............................
# l = '8'
# k = '0123456789'
# res = 0
# for i in range(len(k)):
#     if l == k[i]:
#         res = res*10 +  i 

# print(res)
# print(type(res))


# # finding average.................
# list = [ 1,2,3,4]
# sum = 0
# count =0
# for i in range (len(list)):
#     sum = sum+ list[i]
#     count += 1
# print( "sum ",sum)
# print("count :" ,count)
# print("average :", sum /count)

#validate the registration if user should enter username or email or mobile number .but password and comfirm password must
# user_name = input("enter username :")
# email = input("enter email:")
# mobile_no = input("enter mobile number:")
# password = input("enter mobile password:")
# cnfmpwd = input("enter mobile confirm password:")
# while user_name or email or mobile_no != "":
#     if user_name or email or mobile_no:

#         while password and cnfmpwd != "" :
#             if  password == cnfmpwd :
#                 print("password in validated")
#             else:
#                 print("invalid password")
#     else:
#         print("give correct information")       
# #     

# input_str = "Runika.koosa@123".lower()
# vowel = 0
# num = 0
# consonent = 0
# special_char = 0
# for i in input_str:
#     if i in 'aeiou':
#         vowel += 1
#     elif i.isalpha():
#         consonent += 1
#     elif i == '0123456789':
#         num += 1
#     elif i == '@!$%^&**().,/;#~[]+=_':
#         special_char += 1
    
# print(vowel)  
# print(consonent)
# print(num)
# print(special_char) 


# k = [1,2,3]
# v =[ 'one','two','three']
# j =dict(zip(k,v))
# print(j)

# l =[]
# n = int(input("enter n/o students : "))
# for i in range(1,n+1):
#     j = {}
#     j["pin"] = int(input("enter student pin :"))
#     j["name"] = input("enter student name :")
#     j["fee"] = int(input("enter student fee :"))
#     l.append(j)
#     print(i ,"student added")
#     print(l)
# p = int(input("enter student pin :"))
# for h in l:
#     if h["pin"] ==p :
#         for a,b in h.items():
#             print(a, "===>" ,b)


#k = 'iam going to usa'
#words of length between >2 <5 print

#area of triangle ,rectangle volume of cylinder,cone ,circle

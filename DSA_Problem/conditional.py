# Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

# Return True for the following cases:

# Either a or b (not both) is non-negative and the flag is false.
# Both a and b are negative and the flag is true.

# a = int(input("enter a value : "))
# b = int(input("enter a value : "))
# flag = input(" enter flag(True/False) :")
# if a >0 or b >0 or flag == "True":
#     print(True)
# else:
#     print(False)    

# def two_variables(a,b,flag):
#     if a > 0 or b > 0 or flag == "True":
#         return True
#     else:
#         return False   
# # print(two_variables(-1,-2,False))    


# grid = [['L', 'L', 'W', 'W', 'W'],
#         ['W', 'L', 'W', 'W', 'L'],
#         ['L', 'W', 'W', 'L', 'L'],
#         ['W', 'W', 'W', 'W', 'W'],
#         ['L', 'W', 'L', 'L', 'W']] 
# count = 0 
# for i in range (len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == "L" and grid[i-1][j-1] =="L" or grid[i][j-1] =="L" or grid[i-1][j] =="L": 
#             count += 1
# print(count)           
# 
#  
           
#=============================TWO_SUM_PROBLEMS===================================

# Write a function to check if a string has all unique characters (no duplicates).
# Example:
# s = "abcde" → Output: True
# s = "hello" → Output: False

# def check_string(str):
#     char_str = set()
#     for char in str:
#         if char in char_str:
#             return False
#         char_str.add(char)
#     return True
# print(check_string("runika"))
# print(check_string("ravali"))

# --------method 2 ------------------------
# def is_unique(str):
#     for i in range(0,len(str)):
#         for j in range(i+1,len(str)):
#             if str[i] == str[j]:
#                 print("duplicate string :" , str[i])
#                 return False
#     return True   
         
# print(is_unique("RUNIKA"))
# print()
# print(is_unique("ravali"))

#--------------reversing a string------------------------------------------------
# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str

# print(reverse_string("python")) 
#-------------------------------------------------------------------------
#Print all substrings of a string now? Let me know to continue your easy-level prep systematically.
# def is_substring(str):
#     result = []
#     for i in range(len(str)):
#         for j in range(i,len(str)):
#             result.append(str[i:j+1])
#     return result
# print(is_substring("abcd"))        

##------hashmaping -------------------------
#Given a string, print the frequency of each character in it.
# def freq_string(str):
#     freq ={}
#     for char in str:
#         if char in freq :
#             freq[char] += 1
#         else:
#             freq[char] = 1
#     return freq
# print(freq_string("aaabbbcccccc"))            

##-----------------------------finding largest number in a n array
# def find_max(arr):
#     max_val = arr[0]
#     for num in arr:
#         if num > max_val:
#             max_val = num
#     return max_val
# print(find_max([10,22,33,-33,600]))

##---------------------------fiding second largest number in an array
# def second_largest(arr):
#     if len(arr) < 2:
#         return "invalid "
#     first= second = float('-inf')
#     for num in arr:
#         if num > first:
#             second = first 
#             first = num
#         elif first > num > second :
#             second = num
#     return second if second != float('-inf') else "no second largest"    
# print(second_largest([10,22,44,55,66,77,888,999]))    


#===================check if sorted
# def is_sorted(arr):
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i-1]:
#             return False
#     return True
# print(is_sorted([1,4,6,7,8,9,0]))    

# -------------------------reversing a list

# list = [1,2,3,6,9,11,0,6,55,44,2,1,1,22,7]
# high = len(list)-1
# low = 0
# while low < high:
#     list[low],list[high] = list[high],list[low]
#     low += 1;
#     high -= 1;
# print(list)

#-------------------------sum of all elements in a list
# def sum_ele(arr):
#     sum = 0 
#     for num in arr:
#         sum += num
#     return sum
# print(sum_ele([1,2,3,4,5,6,77]))  
  
#-----------------------------Find duplicates in a list
# def find_dup(arr):
#     dup_list = []
#     for num in arr:
#         if num  

##--------------------2-POINTER PROBLEMS---------------------
#   moving non - zeroes to the end
# def move_zero(list):
#     pos = 0
#     for i in range(0,len(list)):
#         if list[i] != 0:
#             list[pos],list[i] = list[i],list[pos]
#             pos +=1
#     return list
# print(move_zero([1,22,5,0,7,9,0,4,4,0,6]))      
# 

# -----------------------------------------PAIR WITH TARGET SUM
#arr = [1, 2, 3, 4, 6], target = 6

# def target_sum(arr,target):
#     left = 0
#     right = len(arr)-1
#     while left < right :
#         cur_sum = arr[left] + arr[right]
#         if cur_sum == target:
#             return [arr[left], arr[right]]
#         elif cur_sum < target:
#             left +=1
#         elif cur_sum > target:
#             right -= 1
#         else:
#             return "target is not found"
# print(target_sum([1,2,3,6,7,9,10,14] , 16))                

##------------------------------------if we have multiple sum pairs

# def all_pair_sum(arr,target):
#     pair = []
#     left = 0
#     right = len(arr)-1
#     while left < right :
#         cur_sum = arr[left] + arr[right]
#         if cur_sum == target:
#             pair.append ([arr[left], arr[right]])
#             left+=1
#             right -=1
#             while left < right and arr[left] == arr[left - 1]:
#                 left += 1
#             while left < right and arr[right] == arr[right + 1]:
#                 right -= 1
#         elif cur_sum < target:
#             left +=1
#         else:
#             right -=1
#     return pair if pair else "target is not found"
# print(all_pair_sum([1,2,3,6,7,9,10,14] , 16))

##continer with most water
#-----------------------------removing duplicates from a sorted array




# def build_matrix(n):
#     matrix = []
#     for i in range(n):
#         row = []
#         for j in range(n):
#             row.append(0)
#         matrix.append(row)
#     return matrix

# print(build_matrix(3))    

###------------------------Sliding Window (Fixed Size)----------------
#Given an array of integers and a number k, find the maximum sum of a contiguous subarray of size k.
#input : 
# arr = [2, 1, 5, 1, 3, 2]
#k = 3
## output :
#9            ==>>[Explanation: [5,1,3] has the maximum sum = 9]

# def max_sum_subarray(arr,k):
#     start = 0
#     window_max = 0
#     max_sum = float('-inf')
#     for end in range(len(arr)):
#         window_max += arr[end]
#         if end >= k-1 :
#             if window_max > max_sum :
#                 max_sum = window_max
#                 # print(window_max)
#             window_max -= arr[start]
#             start += 1    
#     return max_sum
# print(max_sum_subarray([1,2,4,7,1,4],3))





## -----------------------------find which exact window subarrays are giving the max sum in this sliding window code.

# def max_sum_subarray(arr,k):
#     start = 0
#     window_max = 0
#     max_sum = float('-inf')
#     max_window = []
#     for end in range(len(arr)):
#         window_max += arr[end]
#         if end >= k-1 :
#             if window_max > max_sum :
#                 max_sum = window_max
                
#                 max_window = arr[start:end+1]
#             window_max -= arr[start]
            
#             start += 1    
#     print("Maximum Sum:", max_sum)
#     print("Subarray with Maximum Sum:", max_window)
#     return max_sum
# print(max_sum_subarray([1,2,4,7,1,4],3))

#--------------------print all possible contiguous subarrays.

# def sub_array(arr):
#     n = len(arr)
#     for start in range(n):
#         for end in range(start , n):
#             print(arr[start:end + 1])
  
# sub_array([1,5,7,3,7,2])    


##----------------------subsequences of an array-------------------------------
# def print_subsets(arr, index=0, current=[]):
#     if index == len(arr):
#         print(current)
#         return

#     # Include current element
#     print_subsets(arr, index + 1, current + [arr[index]])

#     # Exclude current element
#     print_subsets(arr, index + 1, current)

# # Test
# print_subsets([1, 2, 3])


#--------------------------------------------------------

#----------------------Smallest Subarray with Sum ≥ Target

#Given an array of positive integers arr and an integer target, 
#find the length of the smallest contiguous subarray whose sum is greater than or equal to target. If no such subarray exists, return 0

#eg   input : arr = [2,3,1,2,4,3]  , target = 7
# def smallest_subarray(arr,target):
#     start = 0
#     window_min = 0 
#     min_sum = float('inf')
#     min_window = []
#     for end in range(len(arr)):
#         window_min += arr[end]
#         while end >= target-1 :
#             if min_sum < window_min :
#                 min_sum = window_min 
#                 min_window = arr[start:end+1]
#                 window_min -= arr[start]   
#                 start += 1
#         else :
#             return 0 

#     return min_sum   
# print(smallest_subarray([2,3,1,2,4,3],7)) 

#---------------------------------------------------------------------------------------
#   Given a string s, find the length of the longest substring without repeating characters.


# def longest_substring(str):
#     char_set = set()   #1. char_set lo current window unique characters store chestham.
#     start = 0
#     max_length = 0
#     result_arr =[]
#     for end in range(len(str)):
#         while str[end] in char_set :  #end pointer move chesthu s[end] ni check chestham.
#     ##If we use if:It checks only once.Suppose duplicate is still 
#     # #present after removing one character, it won’t remove remaining duplicates.
#             char_set.remove(str[start])
#             start +=1                    # 3. If s[end] already in char_set unte:
#                                         # - start pointer increment chesthu,
#                                         # - s[start] ni char_set nunchi remove chestham.
#                                         #    (This removes duplicates from window)
#         char_set.add(str[end])  # 4. Tarvatha s[end] ni add chestham set lo.
#         current_len = end-start+1  # 5. Current window length calculate chesi,
#         if current_len > max_length :    
#             max_length = current_len    #    max_length update chestham if it is greater.
#             result_arr = [str[start:end+1]]   # reset list with new max substring
#         elif current_len == max_length :
#             result_arr.append(str[start:end+1])   

#     print("longest_string lenght : " , max_length)
#     print("longest_strings",result_arr)

# longest_substring("abcdad")    


#---------------------------------------------------------------------------------------------

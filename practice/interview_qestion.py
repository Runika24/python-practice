# data = b'\x48\x65\x6c\x6c\x6f'  # Hex for ASCII "Hello"
# print(data)                     # Output: b'Hello'
# print(type(data))     

# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")

#merginf two lists
# def merge_sorted_lists(list1, list2):
#     merged = []
#     i = j = 0

#     # Merge while both lists have elements
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             merged.append(list1[i])
#             i += 1
#         else:
#             merged.append(list2[j])
#             j += 1

#     # Add remaining elements (if any)
#     merged.extend(list1[i:])
#     merged.extend(list2[j:])
    
#     return merged

# a = [1, 3, 5, 7,1]
# b = [2, 4, 6, 8,9]
# result = merge_sorted_lists(a, b)
# print(result) 


# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         p1 = m - 1  # Pointer for nums1
#         p2 = n - 1  # Pointer for nums2
#         p = m + n - 1  # Pointer for merged array

#         # Merge from the end
#         while p2 >= 0 and p1 >= 0:
#             if nums1[p1] > nums2[p2]:
#                 nums1[p] = nums1[p1]
#                 p1 -= 1
#             else:
#                 nums1[p] = nums2[p2]
#                 p2 -= 1
#             p -= 1

#         # Copy remaining elements from nums2, if any
#         while p2 >= 0:
#             nums1[p] = nums2[p2]
#             p2 -= 1
#             p -= 1

# # Test case
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

# sol = Solution()
# sol.merge(nums1, m, nums2, n)
# print(nums1)  # Output: [1, 2, 2, 3, 5, 6]


# class Solution(object):
#     def removeElement(self, nums, val):
#         i = 0
#         for j in range(len(nums)):
#            if  nums[j] != val:
#             nums[i] = nums[j]
#             i+=1
#         return i;
              
# sol = Solution()
# nums = [3,2,2,3]     
# val = 3 
# k = sol.removeElement(nums,val)
# print(k)
# print(nums[:k])

# class Solution(object):
#     def triangleType(self, nums):
#         i =0
#         n = len(nums)
#         for i in range(n):
#             if nums[0]+nums[1]>nums[2] or nums[0]+nums[2]>nums[1] or nums[1]+nums[2]>nums[0]:
#                 if nums[0] ==nums[1] ==nums[2]:
#                     return "equilateral"
#                 elif nums[0]==nums[1] and nums[0] !=nums[2] or nums[2] == nums[1] and nums[2] !=nums[0] or nums[0] ==nums[2] and nums[0] !=nums[1] :
#                     return "isosceles"
#                 elif nums[0] != nums[1] != nums[2]:
#                     return "scalene"
#         return None            
# sol = Solution()
# nums=[3,3,3]
# k = sol.triangleType(nums)
# print(k)
        
# class Solution(object):
#     def triangleType(self, nums):
#         i =0
#         n = len(nums)
#         for i in range(n):
#             if nums[0]+nums[1]>nums[2] and nums[0]+nums[2]>nums[1] and nums[1]+nums[2]>nums[0]:
#                 if nums[0] == nums[1] and nums[1] == nums[2]:
#                     return "equilateral"
#                 elif nums[0]==nums[1] and nums[0] !=nums[2] or nums[2] == nums[1] and nums[2] !=nums[0] or nums[0] ==nums[2] and nums[0] !=nums[1] :
#                     return "isosceles"
#                 elif nums[0] != nums[1] and nums[1] != nums[2] and nums[0] != nums[2]:
#                     return "scalene"
#             return None            
# sol = Solution()
# nums=[8,4,2]
# k = sol.triangleType(nums)
# print(k)
        



        
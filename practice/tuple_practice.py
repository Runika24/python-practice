#-------------Tuple problems(basic)--------------------

# Q1. Create a tuple of 5 elements and:
# (a) Print the second item
# (b) Slice from index 1 to 3
# (c) Check if a given element exists

# t1 = (1,2,3,4,5)
# print(t1[1])
# print(t1[1:3])
# if 4 in t1 :
#     print("4 is in tuple")
# else:
#     print("4 is not in tuple")    


# Write a program to count how many times a given element appears in a tuple.
# t1 = (1,2,3,4,5)
# count =0
# for i in range(len(t1)):
#     count +=1
# print(count)   
# 
#  Can you change a value inside a tuple? If not, how can you "update" a tuple?
# ****No, you cannot change a value inside a tuple directly because tuples are immutable in Python 
# — once created, their elements cannot be modified, added, or removed.***
# t = (1, 2, 3, 4)

# # Let's say we want to change the 2nd element (index 1) to 99
# t = t[:1] + (99,) + t[2:]

# print(t)   

#Convert a list of numbers to a tuple and back to a list.
# li = [1,2,3,4,56,7]
# t= tuple(li)
# print(t)

#Given the following tuple:
# Can you change any element in this tuple? If so, which and how?
# t = (1, 2, (3, 4), [5, 6])
# t[3][0] = 999
# print(t[3][0])

#  Flattening a Nested List (Recursive) Example
# def flatten(sequence):
#     result = []
#     for item in sequence:
#         # If the item is a list or tuple, recurse into it
#         if isinstance(item, (list, tuple)):
#             result.extend(flatten(item))  # Extend result with flattened items
#         else:
#             result.append(item)  # If it's not a list or tuple, add the item as is
#     return result

# nested_list = [1, [2, [3, 4], 5], 6, (7, 8, [9, 10]), [11, 12]]

# flattened = flatten(nested_list)
# print(flattened)  


sentence = "apple orange apple banana orange apple"
words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


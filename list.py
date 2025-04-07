#WAP to print alla elements in list....................
list = [1,2,3,4,5]
for elements in list:
    print(elements)

#add all elements in a list..............................
list1 = [1,2,3,7,8,9,9,88,999]
sum = 0;
for elements in list1:
    sum += elements;
print(sum)

#adding even elements in the list1.............................
sum=0;
for elements in list1:
    if elements %2 ==0:
        sum += elements;
print(sum)

#adding even indices elements in the list1................
som = 0;
for elements in range(len(list1)):
    if list1[elements] % 2 == 0:
        sum += list1[elements];
print(sum)

### adding even indices element with even number in a list1...............................
sum = 0;
for i in range(len(list1)):
    if i %2 == 0 and list1[i] %2 == 0:
        sum += list1[i]
print(sum)

# finding maximum element in a list...........
li = [1,2,9,-9,7,0,3,2,2,2,1,100]
if len(li) > 0:
    max = li[0] #max =float('-inf')
    for i in li:
        if i > max:
            max = i
print(max)

# # finding minimum element in a list...........
li = [1,2,9,-9,7,0,3,2,2,2,1,100]
if len(li) > 0:
    min = li[0]  
    for i in li:
        if min > i:
            min = i
print(min)

###############finding maximum & minimum element in a list..................
i = [1,2,9,-9,7,0,3,2,2,2,1,100]
if len(li) > 0:
    max = li[0]
    min = li[0]
    for i in li:
        if i > max:
            max = i
    for i in li:
        if min > i:
            min = i              
print(max)
print(min)

###############constant time complexity function or O(N),linear time complexityor O(1), O(n^2) for 2 for loops , O(n^3) for 3 for loops,,,,,,,,,,,
##efficiency order - O(1) > O(logn) eg :binary search algorithm >  O(n) > O(nlogn) >  O(n^2) > O(n^3)
## S.C (SPACE COMPLEXITY) -how much memory is used by the algorithm or to store the data or to run a code or to store the data in the memory
## O(1)- space complexity is constant, O(n) - space complexity is linear, O(n^2) - space complexity is quadratic

list = [1,2,3,4,5,6,7,8,9,10,10,777,6,-33]
dup_list = []
for i in list:
    if i not in dup_list:
        dup_list.append(i)
    else:
        print("duplicate element is:",i)

###--------------------------------------------------------------------------------------------
#---------reverse a list--------------------------
# 1.using inbuilt method
# 2.slicing

list1 = [1,2,3,6]
list1 = list1[::-1]
print(list1)

# 3. using extra memory 
#  
# ----------1st approch-------   
list1 = [1,2,3,6,9]
output_list = []
for i in range(len(list1)-1,-1,-1):
    output_list.append(list1[i])
print(output_list)   

###-----------2nd approuch--------

list1 = [1,2,3,6,9,11]
list0 = []
for i in list1:
    list0.insert(0,i) # =>here 0 is index and i is the value where it is inserted in 2th index..
print(list0)

# using swaping a,b = b,a=>swaping

list = [1,2,3,6,9,11,0,6,55,44,2,1,1,22,7]
high = len(list)-1
low = 0
while low < high:
    list[low],list[high] = list[high],list[low]
    low += 1;
    high -= 1;
print(list)

##-----------------------------------------------------------

#swaping upper half--------------------
list = [1,2,3,6,9,11,0,6,55,44,2,1,1,22]
high = len(list)-1
n = len(list)
low = n//2
while low < high:
    list[low] , list[high] = list[high] , list[low]
    low += 1;
    high -= 1;
print(list)

#-----------------------------------------------------------

##swaping lower half -----------------------
list = [1,2,3,6,9,11,0,6,55,44,2,1,1,22,5,4,3,29]
high = (len(list)-1)//2
n = len(list)
low = 0
while low < high:
    list[low] , list[high] = list[high] , list[low]
    low += 1;
    high -= 1;
print(list)

##-------
#a ,b =10,20  =>multiple assignation of varables
##-----using temperary variable-----
a = 10
b= 12
temp =0
temp = a  #=>temp =10
a = b # => a = 12
b = temp# =>  b=10
print(a,b)

#----------------------------

a,b =1,22
a = a+b
b = a -b
a = a - b
print(a,b)

#--4th way ----  EXOR (^)---------------

a,b =10,13
a = a^b #10^13
b = a^b #10^13^13 => 10^0 => 10
a = a^b #10^13^10 =>13^0 => 13
print(a,b)

#searching  an element
#if the element is present in the list then return True
a =1
list = [1,2,3,6,9,11,0,6,55,44,2,1,1,22,5,4,3,29]
for i in range(0,len(list)):
    if a in list:
        print(a)
        break         #==>>using ternary operator : return True if i in list else False
    else:
        print("not present")

##----------2nd approch----------------------------
def search_ele_list(list,ele):
    if ele in list:
        return True
    else:
        return False       
print(search_ele_list(list, 22))
 #return in which index that element is present,(-1 if not there in the list)

a =1
lis = [1,2,3,6,9,11,0,6,55,44,2,1,1,22,5,4,3,29]
for i in range(0,len(lis)-1):
    if a in lis:
        print(i)
        break
    else:
        print(-1)

#2nd approch---------------
def search_ele_index(lis,elem):
    for i in range(len(lis)):
        if elem ==lis[i]:
            return i
    return -1  
print(search_ele_index(lis,0))         

#linear search algorithm
#time and space complexity -t.c O(n),S.C -O(1)

##-------finding duplicates in a list-------------

list1 = [1,1,2,3,4,55,55,6,7,12,88,76,99,1,2,333,4,555]
visited_list = []
output_list = set() #=> set doesn't allow duplicates
for i in list1:
    if i in visited_list:
        print(i,"is duplicate list") 
        output_list.add(i)  
    else:
        visited_list.append(i)
print(visited_list)
print(output_list)      
#print(list(output_list))

#finding duplicate digit in a given number
    
def check_dup_digit(num) :
    temp = num
    rem = 0
    count =0
    li = []
    while num != 0:
        rem = temp % 10
        if rem in li:
            print(rem)
            return True
        
        else:
            li.append(rem)
    return False
print(check_dup_digit(123445)) 
 
#----------------------------------------------------------------------------------------------------------------------------
list1 = [1221,33,43,44,222]
output_list =[]
for i in list1:
    res = check_dup_digit(i)
    output_list.append(res)
print(output_list)   

#-----------------------------------------------------------------------------------------------------------------------------------

##Binary search algorithm..............
#Binary search is an efficient algorithm for finding a target value within a sorted list. 
#It works by repeatedly dividing the search interval in half.
#firsts we have to rewrite the array in ascending order. 

list_00 = [1,2,3,4,6,8,9,99]
def binary_search (input_list,search_elem):
    low = 0
    high = len(input_list)-1
    while low <= high:
        mid =(low + high)//2
        if input_list == search_elem:
            return mid
        elif input_list[mid] < search_elem:
            low = mid
        else:
            high = mid 
    return -1 #=> elememt not found
print(binary_search(list_00,1))  

##---bubblesort algorithm----------------


#....unoptimized bubblesort.................
list_123 = [1,33,4,22,66,-99,76,55,66]

for j in range((0,len(list_123)-1)):
    for i in range(0,len(list_123)-1):
        if list_123[i]> list_123[i+1]:
            list_123[i],list_123[i+1] = list_123[i+1],list_123[i]
        len(list_123)-1 -=1
print(list_123)
#T.C - O(n square) s.c - O(1)  
#optimized sort-------------
for j in range((0,len(list_123)-1-j)):
    for i in range(0,len(list_123)-1):
        if list_123[i]> list_123[i+1]:
            list_123[i],list_123[i+1] = list_123[i+1],list_123[i]
        len(list_123)-1 -=1
print(list_123)



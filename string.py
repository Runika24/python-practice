#give algebric expression , remove brackets 
## input "a+((b-c)+d)" output :a+b-c+d
input_string = "a+((b-c)+d)"
output_string = ""
for i in input_string:
    if i not in ['(',')','{','}','[',']'] :
        output_string += i   
print(output_string)        
print("----------------------------------")
#--------------------palindrome--------------------------
#check whether a given string is palindrome or not a palindrome 
##inp: mom output : palindrome


##************************************************************************************************************8
#check vowels count, consonent count and space count in a string------
input_str = "Runika.koosa  ".lower()
vowel = 0
space = 0
consonent = 0
other = 0
for i in input_str:
    if i in 'aeiou':
        vowel += 1
    elif i.isalpha():
        consonent += 1
    elif i == ' ':
        space += 1
    else:
        other += 1
    
print(vowel)  
print(consonent)
print(space)
print(other) 
print("----------------------------------")
#***********************************************************************************

#print non repeated vowels from a given input
input ="take u forword is awsome".lower()
for i in 'aeiou':
    if input.count(i) ==1:
        print(i)
print("----------------------------------")        
#-----------------------------
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
for i  in input:
    if i =='a':
        a_count += 1
    elif i =='e':
        e_count += 1
    elif i =='i':
        i_count += 1
    elif i =='o':
        o_count += 1
    elif i =='u':
        u_count += 1                
print(a_count)  
print(e_count) 
print(i_count)  
print(o_count) 
print(u_count) 

print("----------------------------------")
#*************************************************************************************
#find the largest word in a string
#inp : "google docs are better then word docs"
print("find the largest word in a string:")
str1 = 'google docs are better than word docs'
str = (str1.split())
max_length =0
for i in str:    
    if len(i) > max_length:
        max_length = len(i) 
        print(i)     
print(max_length)
#--------------------
for i in str:
    if len(i) ==  max_length:
        print(i)

print("----------------------------------")

##write a program to find a word in a given string that has 
#the highest number of  repeated letters,if not found return -1
#input: "google Microsoft"  out :"google"
#input :"cameron blue" output :-1       


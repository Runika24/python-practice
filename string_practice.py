# Ask the user for their first name and last name. Combine the first 3 letters of the first name 
# and last 3 letters of the last name to create a username.
# Input: First name = "Rahul", Last name = "Sharma"
# Output: Username = "Rahma"
first_name = input("enter the first name : ")
last_name = input("enter the last name : ")
str1 =first_name[ : 3]
n = (len((last_name)))
str2 =last_name[-3: ]
print(f' username: {str1 + str2}')

#Ask the user to enter their email address and check if it contains @ and .com or .in.
# Input: "user@gmail.com"
# # # Output: "Valid email"
user_name = input("Enter the username (email): ")

if "@" in user_name and (user_name.endswith(".com") or user_name.endswith(".in")):
    print("Valid input")
else:
    print("Enter valid mail_id")
      

# Ask the user to enter a message. Count how many words are in the message.
## Input: "Hello there, how are you?"
# Output: 5 words
str =input("enter a message:")
message = (str.split(" "))
print(message)
count =0
for i in message:
    count+=1
print(count)

# Take input of a grocery item name and its price. Show the output in a nicely formatted sentence.
# Input: "Milk", 50
# Output: "Milk costs ₹50"
input_name , input_cost =input("enter the name of product :"),int(input("enter cost of the product :"))
print(f'{input_name} costs ₹{input_cost}')

#  Ask the user to enter a word and check if it is a palindrome (reads the same backward and forward).
# Input: "madam"
# Output: "It is a palindrome."
def check_palindrome(input_str):
    if input_str == input_str[::-1]:
        return "it is a palindrome"
    else:
        return "not a palindrome"
print(check_palindrome("madam"))

# Ask for the full name of a person and print only their initials in uppercase.
# Input: "Virat Kohli"
# Output: "V.K."
full_name =input("enter full name:") 
input1 =full_name.split(" ")
print(input1)
output1 =""
for substr in input1:
    output1 += substr[0].upper()
print(output1)   



#Ask the user to enter their name and check if it contains the letter "a" or any letter you choose.
# Input: "Sanya"
# Output: "Yes, the name contains the letter 'a'"
input_name =  input("enter the name : ")
for i in range (0,len(input_name)):
    if input_name[i] == "a":
        result = "Yes, the name contains the letter 'a' "
        break
    else:
        result = "No,the name doesn't contains the letter 'a' "
print(result)

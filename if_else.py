
# .....................easy level problem solving questions on if,else and ladder if..............
#write a program to check if a number is positive or negative

i = float(input("Enter the number :"))
if i >= 1:
    print("positive")
elif i == 0:
    print("zero")
else:
    print("negative")  

#determine a number is odd or even

num1 = int(input("enter a number :"))     
if num1%2 == 0:
    print("even")
else:
    print("odd")

#   check if a peson is eligibleto vote(age>=18) 

user_age = int(input("enter age :"))
if user_age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")    

 #write a program to find the greatest of two numbers

number1 = int(input("enter number1 :"))
number2 = int(input("enter number2 :"))
if number1 > number2:
    print("number1 is greater than number2")
elif number1 == number2:
    print("number1 is equal to number2")
else:
    print("number1 is less than number2")    
    
# print  "pass" if the student scores more than 40 marks, otherwise print "fail"    
student_marks = int(input("marks scored by a student is "))
if student_marks > 40:
    print("pass")
else:
    print("fail")    
res = "pass" if student_marks>40 else "fail"
print(res)
#   write a program to display the day of the week based on a number input(1.monday.....etc)

day = int(input("number :")) 
if day == 1:
    print("monday")
elif day == 2:
    print("tuesday") 
elif day ==3 :
    print("wednesday")
elif day == 4:
    print("thursday")
elif day == 5:
    print("friday") 
elif day ==6 :
    print("saturday")
elif day ==7:
    print("sunday")    
else :
    print("invalid input")

# impliment a simple calculator to perform addition,multiplication,subtraction and division
    
operation = input("enter operation to perform :").lower()
num1 = float(input("enter first number :"))
num2 = float(input("enter second number :"))
if operation == "add":
    print(num1 + num2)
elif operation == "mul":
    print(num1 * num2)    
elif operation == "div":
    if num2 == 0:
        print("not divisible")
    else:
        print(num1 / num2)
elif operation == "sub":
    print(num1 - num2)
else:
    print("invalid input")           
    
#write a program to clasify whether the string is vowel,consonant or neither

char = input("enetr a single character :").lower()
if len(char) not in [1]: #len(char) != 1
    print("invalid string")
else:
    if char in["a","e","i","o","u"]:
        print("vowel")
    elif char.isalpha():
        #isalpha return boolian true if the string is alphabet
        print("consonant")    
    else:
        print("a special character")     

#Write a program to find the greatest of three numbers.

a = int(input("enter a number1 :"))
b = int(input("enter a number2 :"))
c = int(input("enter a number3 :"))
if a > b and a > c:
    print("a is the greatest number",a)
elif b > a and b > c: 
    print("b is the greatest number",b)
elif c > a and c >b:
    print("c is the greatest number",c)
else:
    print("invlid numbers!!")

    #Check if a year is a leap year.

year = int(input("enter a year : "))
if (year % 4 ==0 and year % 100 != 0) or (year % 400 ==0):
    print("Leap year")
else:
    print("Not a leap year")    

# Calculate the grade of a student based on the marks they score:
#1. 90-100: Grade A
#2. 80-89: Grade B
#3. 70-79: Grade C
#4. <70: Fail.

student_marks = int(input("enter marks of the student :"))
if student_marks >= 90 and student_marks <100:
    print("A grade")
elif student_marks >= 80 and student_marks <90:
    print("B grade")
elif student_marks >= 70 and student_marks <80:
    print("C grade")
elif student_marks >=0 and student_marks<70:
    print("Fail")
else:
    print("invalid input")       

# Write a program to check if three sides length form a valid triangle.

a = float(input("lenght of side 1:"))
b = float(input("lenght of side 2:"))
a = float(input("lenght of side 3:"))
if (a < b + c) and (b < c + a) and (c < b + a):
    print("three sides lenght form a valid triangle");
else:
    print("invalid")

#----------------------------------------------------------------------------

#Write a program to find the greatest of three numbers.

a = int(input("enter a number1 :"))
b = int(input("enter a number2 :"))
c = int(input("enter a number3 :"))
if a > b and a > c:
    print("a is the greatest number",a)
elif b > a and b > c: 
    print("b is the greatest number",b)
elif c > a and c >b:
    print("c is the greatest number",c)
else:
    print("invlid numbers!!")

    #Check if a year is a leap year.

year = int(input("enter a year : "))
if (year % 4 ==0 and year % 100 != 0) or (year % 400 ==0):
    print("Leap year")
else:
    print("Not a leap year")    

# Calculate the grade of a student based on the marks they score:
#1. 90-100: Grade A
#2. 80-89: Grade B
#3. 70-79: Grade C
#4. <70: Fail.

student_marks = int(input("enter marks of the student :"))
if student_marks >= 90 and student_marks <100:
    print("A grade")
elif student_marks >= 80 and student_marks <90:
    print("B grade")
elif student_marks >= 70 and student_marks <80:
    print("C grade")
elif student_marks >=0 and student_marks<70:
    print("Fail")
else:
    print("invalid input")       

# Write a program to check if three sides length form a valid triangle.

a = float(input("lenght of side 1:"))
b = float(input("lenght of side 2:"))
a = float(input("lenght of side 3:"))
if (a < b + c) and (b < c + a) and (c < b + a):
    print("three sides lenght form a valid triangle");
else:
    print("invalid")
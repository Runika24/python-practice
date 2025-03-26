#Write a program to display the multiplication table of a given number. First 20
number=int(input("enter the number:"))
def multiplication_table(num):
    print(f"Multiplication Table of {num} (First 20):")
    for i in range(1, 21):
        print(f"{num} x {i} = {num * i}")
multiplication_table(number)

#Write a program to calculate the factorial of a number using a while loop. 

number = int(input("Enter a number: "))
def factorial(num):
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result
print(f"Factorial of {number} is {factorial(number)}")
    
#Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.
def divisible_by_3_and_5():
    print("Numbers from 1 to 100 that are divisible by 3 and 5:")
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(num)

divisible_by_3_and_5()
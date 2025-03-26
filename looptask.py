
#------wap to print the sum of odd digits in a number
def sum_of_odd_digits(number):
    sum_odd = 0
    while number > 0:
        digit = number % 10
        if digit % 2 != 0:
            sum_odd += digit
        number //= 10
    return sum_odd
print(sum_of_odd_digits(12674))

# Print all the Armstrong numbers in given range
def is_amstrong_number(num):
    temp = num;
    sum = 0;
    n = len(str(num))
    while temp > 0:
        rem = temp % 10
        pow = rem**n;
        sum += pow
        temp //= 10
    if (sum == num):    
        return num
def armstrong_in_range(a, b):
    for num in range(a, b + 1):
        if is_amstrong_number(num):
            print(num, end=" ")


a = int(input("Enter start of range: "))
b = int(input("Enter end of range: "))

print(f"Armstrong numbers between {a} and {b}:")
armstrong_in_range(a, b)    

#Find the smallest prime digit in a given number

def smallest_prime_digit(num):
    prime_digits = {2, 3, 5, 7}  
    min_prime = float('inf')  

    while num > 0:
        digit = num % 10
        if digit in prime_digits:
            min_prime = min(min_prime, digit)
        num //= 10

    return min_prime if min_prime != float('inf') else -1  

# Input from user
num = int(input("Enter a number: "))
result = smallest_prime_digit(num)

if result != -1:
    print("Smallest prime digit:", result)
else:
    print("No prime digit found in the number")

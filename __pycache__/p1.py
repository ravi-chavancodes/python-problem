# Hello World Program
"""
print("Hello, World!")

# Basic Arithmetic Operations

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Exponent =", a ** b)
"""

# 2q implementing conditional statements and loops for simple prrogrrams  
"""
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
    """

# 3q - writing functions to perform basic calculations eg - factorial , ffibonacci
#a.factorial 
"""
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact


num = int(input("Enter a number: "))
print("Factorial =", factorial(num))
"""

#b. fibonacci 

"""
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c


num = int(input("Enter the number of terms: "))
fibonacci(num)
"""
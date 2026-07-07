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

# Practical No. 2

#Question:
#Implementing Conditional Statements and Loops for Simple Programs.

#Aim:
#To write a Python program using conditional statements and loops. 

# Program:
"""
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

print("Numbers from 1 to 10 are:")

for i in range(1, 11):
    print(i)
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

#4 Program to Find Prime Numbers Using Functions and Loops

# Function to check prime number
"""
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# Main Program
num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")
    """

#5 Designing and Implementing a Simple Calculator Application Using Functions and Control Structures
"""
# Function Definitions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b

# Main Program
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(num1, num2))

elif choice == 2:
    print("Result =", subtract(num1, num2))

elif choice == 3:
    print("Result =", multiply(num1, num2))

elif choice == 4:
    print("Result =", divide(num1, num2))

else:
    print("Invalid Choice")
    """

#6 Implementing a Program to Convert Temperature Units (Celsius to Fahrenheit) Using Functions
"""
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Main Program
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)

print("Temperature in Fahrenheit =", fahrenheit)
"""

# Practical No. 7

# Question: Creating and Manipulating Lists to Store and Process Data (e.g., Sorting, Searching).

# Aim: To write a Python program to create a list and perform sorting and searching operations.

# Program:
"""
numbers = [45, 12, 78, 23, 56]

print("Original List:", numbers)

numbers.sort()
print("Sorted List:", numbers)

key = int(input("Enter element to search: "))

if key in numbers:
    print(key, "found in the list")
else:
    print(key, "not found in the list")
    """

# Practical No. 8

# Question:Implementing a Program to Find the Maximum and Minimum Elements in a List.

# Aim: To write a Python program to find the maximum and minimum elements in a list.

# Program:
"""
numbers = [45, 12, 78, 23, 56]

print("List:", numbers)

print("Maximum Element =", max(numbers))
print("Minimum Element =", min(numbers))
"""

# Practical No. 9

# Question: Working with Dictionaries to Store and Retrieve Data Efficiently.

# Aim: To write a Python program to store and retrieve data using a dictionary.

# Program:
"""
student = {
    "Name": "Ravi",
    "Roll No": 101,
    "Marks": 85
}

print("Student Details")
print("Name:", student["Name"])
print("Roll No:", student["Roll No"])
print("Marks:", student["Marks"])
"""
# Practical No. 10

# Question: Implementing List Comprehensions for Efficient Data Processing.

# Aim: To write a Python program using list comprehension to generate the squares of numbers.

# Program:
"""
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print("Original List:", numbers)
print("Squares:", squares)
"""
#11. Polymorphism in Python

"""
# Parent Class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child Class 1
class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Child Class 2
class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Creating Objects
d = Dog()
c = Cat()

# Calling Methods
d.sound()
c.sound()
"""

#12. Encapsulation in Python

"""
# Class
class Student:
    def __init__(self):
        self.__marks = 90    # Private variable

    def display(self):
        print("Marks =", self.__marks)

# Creating Object
s = Student()

# Calling Method
s.display()
"""

#
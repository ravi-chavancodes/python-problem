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

#Program:

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

print("Numbers from 1 to 10 are:")

for i in range(1, 11):
    print(i)

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

#7. File Handling – Read and Write Data to a File

"""
# Write data to a file
file = open("student.txt", "w")
file.write("Hello World\n")
file.write("Welcome to Python File Handling")
file.close()

# Read data from the file
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()
"""

#8 Exception Handling – Handling Errors Using try, except, and finally

"""
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numbers.")

finally:
    print("Program Executed Successfully.")
"""

#9. Object-Oriented Programming (OOP) – Create a Class and Object

"""
# Class Definition
class Student:

    # Constructor
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    # Method
    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll)

# Creating Object
s1 = Student("Ravi", 101)

# Calling Method
s1.display()
"""

#10. Implementing Inheritance in Python

"""
# Parent Class
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

# Child Class
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def show(self):
        self.display()
        print("Roll Number:", self.roll)

# Creating Object
s = Student("Ravi", 101)

# Calling Method
s.show()
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
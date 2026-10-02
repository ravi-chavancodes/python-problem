# Hello World Program
"""
print("Hello World")

a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

"""
# Practical No. 2

#Question:
#Implementing Conditional Statements and Loops for Simple Programs.

#Aim:
#To write a Python program using conditional statements and loops. 
"""
n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

print("Numbers from 1 to", n)

for i in range(1, n + 1):
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
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter limit: "))

for i in range(2, n + 1):
    if is_prime(i):
        print(i, end=" ")
"""
#5 Designing and Implementing a Simple Calculator Application Using Functions and Control Structures
"""
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", add(a, b))

elif choice == 2:
    print("Result:", subtract(a, b))

elif choice == 3:
    print("Result:", multiply(a, b))

elif choice == 4:
    print("Result:", divide(a, b))

else:
    print("Invalid choice")
    
"""

#6 Implementing a Program to Convert Temperature Units (Celsius to Fahrenheit) Using Functions. # implement (fahrenheit to celsius)
"""
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

c = float(input("Enter Celsius: "))
print("Fahrenheit:", celsius_to_fahrenheit(c))

f = float(input("Enter Fahrenheit: "))
print("Celsius:", fahrenheit_to_celsius(f))
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

# Question:Implementing a Program to Find the Maximum and Minimum Elements in a List.( with input)

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

# Question: Implementing List Comprehensions for Efficient Data Processing .

# Aim: To write a Python program using list comprehension to generate the squares of numbers.

# Program:
"""
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print("Original List:", numbers)
print("Squares:", squares)
"""
# Practical No. 11

# Question: Implementing Exception Handling to Handle Errors Gracefully.

# Aim: To write a Python program to handle exceptions using try and except.

# Program:
"""
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input.")
"""

# Practical No. 12

# Question:Creating a Basic Class Hierarchy to Demonstrate Object-Oriented Programming Concepts.

# Aim:To write a Python program to demonstrate inheritance using a basic class hierarchy.

# Program:
"""
class Shape:
    def area(self):
        print("Area of shape")

class Rectangle(Shape):
    def area(self):
        l = 10
        b = 5
        print("Rectangle area:", l * b)

class Circle(Shape):
    def area(self):
        r = 5
        print("Circle area:", 3.14 * r * r)

r = Rectangle()
c = Circle()

r.area()
c.area()
"""

# Practical No. 13

# Question: Reading Data from a Text File and Performing Simple Analysis (e.g., Word Count).

# Aim: To write a Python program to read data from a text file and count the number of words.

# Program:
"""
file = open("sample.txt", "r")

text = file.read()

words = text.split()

print("Number of words =", len(words))

file.close()
"""

# Practical No. 14

# Question: Writing Data to a Text File and Saving User Inputs.

# Aim: To write a Python program to take user input and save it into a text file.

# Program:
"""
text = input("Enter text: ")

file = open("sample.txt", "w")

file.write(text)

file.close()

print("Data saved successfully.")
"""
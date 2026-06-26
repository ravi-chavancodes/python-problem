# print 
"""
print("Hello World")
print("Welcome to Python")
print(10)
print(10 + 20)
"""

# variable 
"""
name = "Ravi"
age = 21
height = 5.8

print(name)
print(age)
print(height)

"""

# data type
"""
name = "Ravi"
age = 21
salary = 50000.50
is_student = True

print(type(name))
print(type(age))
print(type(salary))
print(type(is_student))

"""

# input

"""
name = input("Enter name: ")
age = int(input("Enter age: "))

print("Name:", name)
print("Age:", age)

"""

# operator
"""
a = 10
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)
"""

# if else

"""
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
    """

# loop

"""

for i in range(1, 6):
    print(i)

count = 1

while count <= 5:
    print(count)
    count += 1
    """
#  pattern 
"""
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()
    """

# string 

"""
text = "Python"

print(text.upper())
print(text.lower())
print(text.replace("Python", "Java"))
print(len(text))

"""

# list

"""
fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")

print(fruits)
print(fruits[0])
"""


# tuples
"""

data = (10, 20, 30)

print(data)
print(data[1])
"""

# sets
"""

numbers = {1, 2, 3, 3, 4}

print(numbers)
"""

# dictonary
"""
student = {
    "name": "Ravi",
    "age": 21
}

print(student["name"])
print(student["age"])
"""

# function
"""
def greet(name):
    print("Hello", name)

greet("Ravi")
"""

# relational
"""
a = 20
b = 10

a += 2
print (a)

b-= 2
print (b)

"""

# logical
"""
a=30
b=20

c = a > b
print(bool(c))
print(not c)
"""

# or
"""
a = 10
b= 5
print(a < 5 or b>2) 
print (a < 5 or b< 2)
"""

#bitwise
"""
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)


"""

# if els 
"""
age = 19
if age >= 20:
    print("Eligible for voting")
else:
    print("not eligible for voting")

"""

#if-elif-else statement
#syntax
"""
marks = int(input("Enter your marks"))
marks = 85
if marks >= 90:
    print("grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
 print("fail")
 """

#nested if-else statement
""""
age = int(input("Enter your age"))
citizen = input("Enter your citizenship")
if age >= 20 and citizen:
    print("Eligible")
else:
    print("Not eligible")

"""

# vowel
"""
text = input("Enter a string: ")

count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)
"""

# square
"""
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()
    """

# row and column 
"""
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()
 """

# every element 
"""
numbers = [1, 2, 3]

for i in numbers:
    for j in numbers:
    print(i, j)
"""

# nested work
"""
for i in range(2):
    for j in range(3):
        print(i, j)
        """
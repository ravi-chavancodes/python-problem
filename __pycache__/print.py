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


fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")

print(fruits)
print(fruits[0])



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

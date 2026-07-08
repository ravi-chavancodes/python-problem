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
for i in range(3):
    for j in range(3):
        print(i, j)
    """    

# break - it will break the loop when condition is satisfied 
#continue - it will egnore the value specified in the condtion when the the condition is matched
"""
name= "vedant"

for i in name :
    print (i)
    """

# pass - it will print nothing when the condition is satisfied
"""
name = "vedant"

for i in name :
    if i =='e':
        pass  # print()
"""
#
"""
price = [100,200,300]

for i in enumerate(price):
    print (i)
    """
# Nested Loop

"""
for i in range(3):
    for j in range(3):
        print(i, j)
"""


# Print Characters of String

"""
name = "vedant"

for i in name:
    print(i)
"""


# Break

"""
name = "vedant"

for i in name:
    if i == 'a':
        break
    print(i)
"""


# Continue

"""
name = "vedant"

for i in name:
    if i == 'a':
        continue
    print(i)
"""


# Pass

"""
name = "vedant"

for i in name:
    if i == 'a':
        pass
    print(i)
"""


# Enumerate

"""
price = [100, 200, 300]

for i in enumerate(price):
    print(i)
"""
# Nested Loop
# Used when one loop runs inside another loop.

"""
for i in range(3):
    for j in range(3):
        print(i, j)
"""


# Print Characters of String
# Prints each character of the string one by one.

"""
name = "vedant"

for i in name:
    print(i)
"""


# Break
# Stops the loop when the condition is true.

"""
name = "vedant"

for i in name:
    if i == 'a':
        break
    print(i)
"""


# Continue
# Skips the current iteration when the condition is true.

"""
name = "vedant"

for i in name:
    if i == 'a':
        continue
    print(i)
"""


# Pass
# Does nothing when the condition is true.

"""
name = "vedant"

for i in name:
    if i == 'a':
        pass
    print(i)
"""


# Enumerate
# Prints both index and value of a list.

"""
price = [100, 200, 300]

for i in enumerate(price):
    print(i)
"""


# Enumerate (Index and Value)
# Stores index and value in separate variables.

"""
price = [100, 200, 300]

for index, value in enumerate(price):
    print(index, value)
"""


# Square Pattern
# Prints a square of stars using nested loops.

"""
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()
"""


# Rectangle Pattern
# Prints a rectangle of stars.

"""
for i in range(3):
    for j in range(5):
        print("*", end=" ")
    print()
"""


# Left Triangle
# Prints a left-aligned triangle.

"""
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
"""


# Inverted Triangle
# Prints an upside-down triangle.

'''
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
'''


# Number Triangle
# Prints numbers from 1 to the current row.

"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
"""


# Same Number Pattern
# Prints the row number multiple times.

"""
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()
"""


# Floyd's Triangle
# Prints continuous numbers in triangle form.

"""
num = 1

for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
"""

# Alphabet Triangle
# Prints alphabets in a triangle pattern.

"""
for i in range(1, 5):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
"""

# Multiplication Table
# Prints a multiplication table from 1 to 5.

"""
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()
"""

# simple intrest
"""
def calculate_sip(principal,rate,time):

    intrest = (principal*rate*time)/100
    return intrest
result = calculate_sip(1000,7.5,3)
print(result)
"""

#positional and keyword call
"""
def dec_pet(animal_type,pet_name):
    print(f"i have a {animal_type}named{pet_name}.")

    """
   
# default
"""
def greet(animal_type,pet_name="hey"):
    return f"{animal_type},{pet_name}"
print(greet("amit"))
print(greet("amit","hello"))
"""

# *args and kwargs 

def analyze(instruct,*student,**data):
    print(f"inst:{instruct}")
    print(f"student tuple:{student}")
    print(f"datano:{data}")


analyze("dr,ji","alice","bob","crcile",romm = 402,subject="py")
"""
Prime Number Checker

This program checks whether a given number is prime or not.

Concepts Covered:
- Functions
- Loops
- Conditional Statements
- Modulus Operator
"""

def is_prime(num):
    """Returns True if the number is prime, otherwise False."""

    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is Prime")
else:
    print(number, "is Not Prime")

# ----------------------------------------
#  Numbers in Python
# ----------------------------------------

# Types of Numbers

# 1. Integers: Whole numbers
num1 = -3
num2 = 0
num3 = 100
print("Integers:", num1, num2, num3)
print("Integers:", num1 + num2 + num3)
print("Integers:", num1- num2+num3)
# 2. Floating-point numbers: Numbers with decimals
pi = 3.14
negative_float = -2.5
print("Floating-point numbers:", pi, negative_float)


# ----------------------------------------
# Basic Arithmetic Operations
# ----------------------------------------

# Addition
add_result = 2 + 3
print("Addition (2 + 3):", add_result)  # 5
num1=9
num2=8
print(num1 +num2)
# Subtraction
sub_result = 5 - 2
print("Subtraction (5 - 2):", sub_result)  # 3
num1=9
num2=8
print(num1 - num2)
# Multiplication
mul_result = 4 * 3
print("Multiplication (4 * 3):", mul_result)  # 12
num1=9
num2=8
print(num1 * num2)

# Division
div_result = 10 / 2
print("Division (10 / 2):", div_result)  # 5.0
num1=9
num2=8
print(num1 / num2)

# Floor Division (discard decimal part)
floor_div_result = 7 // 2
print("Floor Division (7 // 2):", floor_div_result)  # 3

# Modulo (remainder of division)
mod_result = 7 % 2
print("Modulo (7 % 2):", mod_result)  # 1
num1=9
num2=8
print(num1 % num2)

# Exponentiation (power)
exp_result = 2 ** 3
print("Exponentiation (2 ** 3):", exp_result)  # 8
num1=9
num2=8
print(num1 ** num2)


# Example combining them all:
a = 9
b = 4
print("\nExample Calculations:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# more notes on numbers below
# ----------------------------------------
# Arithmetic Operations and Math Functions in Python
# ----------------------------------------

x = 1
y = 2
z = 3

# PEMDAS Order of Operations Example
result = (x + y) * z - (y / x)
print(f"Result: {result}")

# ----------------------------------------
# Basic Arithmetic Operations
# ----------------------------------------

# Division
print(f"Division: {y / x}")

# Addition
print(f"Addition: {x + y}")

# Multiplication
print(f"Multiplication: {(x + y) * z}")

# Subtraction
print(f"Subtraction: {(x + y) * z - (y / x)}")

# Modulo (remainder)
print(f"Modulo: {y % x}")  # The remainder of y divided by x

# Power (exponentiation)
print(f"Power: {x ** y}")

# Absolute Value
print(f"Absolute Value: {abs(x - y)}")

# Max and Min
print(f"Max: {max(x, y, z)}")
print(f"Min: {min(x, y, z)}")

# ----------------------------------------
# Math Library Functions
# ----------------------------------------

# Rounding a number
pi = 3.1415926535
print(f"Round: {round(pi)}")

# Importing math functions
from math import *

print(f"Square Root of 16: {sqrt(16)}")
print(f"Ceiling of Pi: {ceil(pi)}")
print(f"Floor of Pi: {floor(pi)}")







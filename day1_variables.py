"""
Day 1: Python Variables and Data Types
Learn: Variables, integers, floats, strings, booleans, basic operations
"""

# ====================
# Exercise 1: Variables and Basic Operations
# ====================

# TODO: Create variables for your name (string), age (integer), height (in ft), and is_student (boolean)
name = "Morgan Franklin"
age = 28
height = 5.3
is_student = False

# TODO: Print them in a formatted string
print(f"My name is {name}, I'm {age} years old, {height}ft tall.")
print(f"Am I a student? {is_student}")

# TODO: Calculate and print your age in days (assume 365 days/year)
age_in_days = age * 365
print(f"I am approximately {age_in_days} days old")

# TODO: Calculate your age in hours
age_in_hours = age_in_days * 24
print(f"That's {age_in_hours} hours!")

# ====================
# Exercise 2: Temperature Converter
# ====================

# TODO: Create a variable for temperature in Celsius
celsius = 25

# TODO: Convert to Fahrenheit using formula: (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")

# TODO: Convert to Kelvin using formula: C + 273.15
kelvin = celsius + 273.15
print(f"{celsius}°C is {kelvin}K")

# ====================
# Exercise 3: Data Types
# ====================

# TODO: Create variables of different types and print their type
integer_var = 42
float_var = 3.14
string_var = "Hello, Python!"
boolean_var = True
list_var = [1, 2, 3, 4, 5]

print(f"Type of {integer_var}: {type(integer_var)}")
print(f"Type of {float_var}: {type(float_var)}")
print(f"Type of '{string_var}': {type(string_var)}")
print(f"Type of {boolean_var}: {type(boolean_var)}")
print(f"Type of {list_var}: {type(list_var)}")

# ====================
# Exercise 4: Basic Math Operations
# ====================

x = 10
y = 3

print(f"\nMath with {x} and {y}:")
print(f"Addition: {x} + {y} = {x + y}")
print(f"Subtraction: {x} - {y} = {x - y}")
print(f"Multiplication: {x} * {y} = {x * y}")
print(f"Division: {x} / {y} = {x / y}")
print(f"Floor Division: {x} // {y} = {x // y}")
print(f"Modulus: {x} % {y} = {x % y}")
print(f"Exponent: {x} ** {y} = {x ** y}")

print("\n✅ Day 1 Variables Exercise Complete!")
"""
Day 2: Python Conditionals (If/Else Statements)
Learn: Boolean logic, if/elif/else, comparison operators, logical operators
"""

# ====================
# Exercise 1: Basic If/Else
# ====================

print("=== Exercise 1: Basic If/Else ===\n")

# TODO: Create a variable for age and check voting eligibility
age = 28  # Change this to test different ages

if age >= 18:
    print(f"Age {age}: You can vote!")
else:
    print(f"Age {age}: You cannot vote yet.")

# TODO: Check if a number is positive, negative, or zero
number = 0  # Try different numbers

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")

# ====================
# Exercise 2: Comparison Operators
# ====================

print("\n=== Exercise 2: Comparison Operators ===\n")

x = 10
y = 5

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")  # Equal to
print(f"x != y: {x != y}")  # Not equal to
print(f"x > y: {x > y}")    # Greater than
print(f"x < y: {x < y}")    # Less than
print(f"x >= y: {x >= y}")  # Greater than or equal to
print(f"x <= y: {x <= y}")  # Less than or equal to

# ====================
# Exercise 3: Logical Operators (and, or, not)
# ====================

print("\n=== Exercise 3: Logical Operators ===\n")

# TODO: Check if user can access admin panel
username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("✅ Access granted - Welcome Admin!")
else:
    print("❌ Access denied - Invalid credentials")

# TODO: Check if number is in valid range (1-100)
score = 85

if score >= 1 and score <= 100:
    print(f"Score {score} is valid")
else:
    print(f"Score {score} is invalid - must be between 1 and 100")

# Better way using chained comparison:
if 1 <= score <= 100:
    print(f"Score {score} is valid (using chained comparison)")

# TODO: Check if it's a weekend
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print(f"{day} is a weekend!")
else:
    print(f"{day} is a weekday")

# Using 'not' operator
is_logged_in = False

if not is_logged_in:
    print("Please log in to continue")
else:
    print("Welcome back!")

# ====================
# Exercise 4: Grade Calculator
# ====================

print("\n=== Exercise 4: Grade Calculator ===\n")

# TODO: Determine letter grade based on score
score = 85  # Try different scores: 95, 75, 65, 55, 45

if score >= 90:
    grade = "A"
    message = "Excellent!"
elif score >= 80:
    grade = "B"
    message = "Good job!"
elif score >= 70:
    grade = "C"
    message = "Satisfactory"
elif score >= 60:
    grade = "D"
    message = "Needs improvement"
else:
    grade = "F"
    message = "Failed"

print(f"Score: {score} → Grade: {grade} - {message}")

# ====================
# Exercise 5: Leap Year Checker
# ====================

print("\n=== Exercise 5: Leap Year Checker ===\n")

# A year is a leap year if:
# - Divisible by 4 AND not divisible by 100
# - OR divisible by 400

year = 2024  # Try: 2024, 2023, 2000, 1900

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is NOT a leap year")

# ====================
# Exercise 6: Password Strength Checker
# ====================

print("\n=== Exercise 6: Password Strength Checker ===\n")

password = "Test123!"  # Try different passwords

# Check password requirements
has_uppercase = any(c.isupper() for c in password)
has_lowercase = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)
is_long_enough = len(password) >= 8

print(f"Password: {password}")
print(f"✓ Has uppercase: {has_uppercase}")
print(f"✓ Has lowercase: {has_lowercase}")
print(f"✓ Has digit: {has_digit}")
print(f"✓ Has special char: {has_special}")
print(f"✓ At least 8 chars: {is_long_enough}")

if has_uppercase and has_lowercase and has_digit and has_special and is_long_enough:
    print("Password is STRONG")
elif is_long_enough and (has_uppercase or has_lowercase) and has_digit:
    print("Password is MEDIUM")
else:
    print("Password is WEAK")

# ====================
# Exercise 7: Nested If Statements
# ====================

print("\n=== Exercise 7: Nested If - Ticket Pricing ===\n")

age = 28
is_student = True

# Determine ticket price
if age < 5:
    price = 0
    category = "Free (Under 5)"
elif age < 18:
    if is_student:
        price = 8
        category = "Student (Under 18)"
    else:
        price = 10
        category = "Youth"
elif age < 65:
    if is_student:
        price = 12
        category = "Student (Adult)"
    else:
        price = 15
        category = "Adult"
else:
    price = 10
    category = "Senior (65+)"

print(f"Age: {age}, Student: {is_student}")
print(f"Category: {category}")
print(f"Price: ${price}")

print("\n✅ Day 2 Conditionals Exercise Complete!")
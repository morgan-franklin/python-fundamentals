"""
Day 1: Python Strings
Learn: String manipulation, methods, slicing, formatting
"""

# ====================
# Exercise 1: String Basics
# ====================

# TODO: Create variables for first and last name
first_name = "Morgan"
last_name = "Franklin"

# TODO: Combine them into full name
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# TODO: Convert to uppercase and lowercase
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")

# TODO: Get the length of the full name
print(f"Length: {len(full_name)} characters")

# ====================
# Exercise 2: String Methods
# ====================

# TODO: Clean up this messy email
email = "  Morgan.Franklin@EXAMPLE.com  "
cleaned_email = email.strip().lower()
print(f"Cleaned email: {cleaned_email}")

# TODO: Check if email contains @ symbol
has_at = "@" in cleaned_email
print(f"Email has @ symbol: {has_at}")

# TODO: Split email into username and domain
username, domain = cleaned_email.split("@")
print(f"Username: {username}")
print(f"Domain: {domain}")

# ====================
# Exercise 3: String Slicing
# ====================

message = "Python is awesome for test automation"

# TODO: Extract "Python"
print(f"First word: {message[0:6]}")

# TODO: Extract "awesome"
print(f"Awesome: {message[10:17]}")

# TODO: Extract "automation"
print(f"Last word: {message[-10:]}")

# TODO: Get every 2nd character
print(f"Every 2nd char: {message[::2]}")

# TODO: Reverse the string
print(f"Reversed: {message[::-1]}")

# ====================
# Exercise 4: String Formatting
# ====================

name = "Morgan"
role = "QA Engineer"
experience_years = 5

# TODO: Use f-strings to create a professional introduction
intro = f"Hi, I'm {name}, a {role} with {experience_years} years of experience."
print(intro)

# TODO: Create a multi-line formatted string
profile = f"""
Name: {name}
Role: {role}
Experience: {experience_years} years
Skills: Python, Playwright, pytest
"""
print(profile)

# ====================
# Exercise 5: Practical Example - Password Validator
# ====================

password = "TestPass123!"

# TODO: Check password requirements
has_uppercase = any(c.isupper() for c in password)
has_lowercase = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)
is_long_enough = len(password) >= 8

print(f"\nPassword validation for '{password}':")
print(f"Has uppercase: {has_uppercase}")
print(f"Has lowercase: {has_lowercase}")
print(f"Has digit: {has_digit}")
print(f"Has special character: {has_special}")
print(f"Is long enough (8+ chars): {is_long_enough}")

is_valid = has_uppercase and has_lowercase and has_digit and has_special and is_long_enough
print(f"Password is valid: {is_valid}")

print("\n✅ Day 1 Strings Exercise Complete!")
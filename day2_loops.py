"""
Day 2: Python Loops
Learn: for loops, while loops, range(), break, continue
"""

# ====================
# Exercise 1: Basic For Loop
# ====================

print("=== Exercise 1: Basic For Loop ===\n")

# TODO: Print numbers 1 to 10
print("Numbers 1-10:")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# TODO: Print even numbers 2 to 20
print("Even numbers 2-20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

# ====================
# Exercise 2: Looping Through Lists
# ====================

print("\n=== Exercise 2: Looping Through Lists ===\n")

# TODO: Loop through a list of fruits
fruits = ["apple", "banana", "cherry", "grape", "elderberry"]

print("Fruits:")
for fruit in fruits:
    print(f"- {fruit}")

# TODO: Loop with index using enumerate()
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# TODO: Loop through a list of numbers and sum them
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(f"\nNumbers: {numbers}")
print(f"Sum: {total}")
print(f"Average: {total / len(numbers)}")

# ====================
# Exercise 3: While Loop
# ====================

print("\n=== Exercise 3: While Loop ===\n")

# TODO: Countdown from 10 to 1
count = 10
print("Countdown:")
while count > 0:
    print(count, end=" ")
    count -= 1
print("Blast off! \n")

# TODO: Keep asking until correct password
attempts = 0
max_attempts = 3
correct_password = "python123"

print("Password challenge (hint: python123):")
while attempts < max_attempts:
    password = input(f"Enter password (attempt {attempts + 1}/{max_attempts}): ")

    if password == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print(f"Wrong password. {max_attempts - attempts} attempts remaining.")
        else:
            print("Account locked. Too many failed attempts.")

# ====================
# Exercise 4: Break and Continue
# ====================

print("\n=== Exercise 4: Break and Continue ===\n")

# TODO: Find first number divisible by 7 and 5
print("Finding first number divisible by both 7 and 5:")
for num in range(1, 100):
    if num % 7 == 0 and num % 5 == 0:
        print(f"Found it: {num}")
        break

# TODO: Print odd numbers 1-20 (skip even numbers)
print("\nOdd numbers 1-20 (using continue):")
for num in range(1, 21):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num, end=" ")
print("\n")

# ====================
# Exercise 5: Nested Loops
# ====================

print("\n=== Exercise 5: Nested Loops ===\n")

# TODO: Multiplication table
print("Multiplication table (1-5):")
print("    ", end="")
for i in range(1, 6):
    print(f"{i:4}", end="")
print("\n" + "-" * 25)

for i in range(1, 6):
    print(f"{i} | ", end="")
    for j in range(1, 6):
        print(f"{i * j:4}", end="")
    print()

# TODO: Print a pattern
print("\nPattern:")
for i in range(1, 6):
    print("* " * i)

# ====================
# Exercise 6: FizzBuzz Challenge
# ====================

print("\n=== Exercise 6: FizzBuzz ===\n")

# Classic programming problem:
# Print numbers 1-30
# If divisible by 3: print "Fizz"
# If divisible by 5: print "Buzz"
# If divisible by both: print "FizzBuzz"
# Otherwise: print the number

print("FizzBuzz (1-30):")
for num in range(1, 31):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=" ")
    elif num % 3 == 0:
        print("Fizz", end=" ")
    elif num % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(num, end=" ")
print("\n")

# ====================
# Exercise 7: Practical Example - Sum of Even Numbers
# ====================

print("\n=== Exercise 7: Sum of Even Numbers 1-100 ===\n")

# Method 1: Using for loop
total = 0
for i in range(2, 101, 2):
    total += i
print(f"Sum (using for loop): {total}")

# Method 2: Using while loop
total = 0
i = 2
while i <= 100:
    total += i
    i += 2
print(f"Sum (using while loop): {total}")

# Method 3: Using sum() and range()
total = sum(range(2, 101, 2))
print(f"Sum (using sum function): {total}")

# ====================
# Exercise 8: List Comprehension Preview
# ====================

print("\n=== Exercise 8: List Comprehension (Advanced) ===\n")

# Traditional way:
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(f"Squares (traditional): {squares}")

# List comprehension way (more Pythonic):
squares = [i ** 2 for i in range(1, 11)]
print(f"Squares (comprehension): {squares}")

# Filter even numbers
evens = [i for i in range(1, 21) if i % 2 == 0]
print(f"Evens 1-20: {evens}")

# ====================
# Exercise 9: Real-World Example - API Testing Loop
# ====================

print("\n=== Exercise 9: API Testing Simulation ===\n")

# Simulate checking API endpoints
endpoints = [
    {"url": "/api/users", "expected_status": 200},
    {"url": "/api/products", "expected_status": 200},
    {"url": "/api/orders", "expected_status": 404},  # Intentional fail
    {"url": "/api/login", "expected_status": 200},
]

# Simulate testing each endpoint
import random

passed = 0
failed = 0

print("Testing API endpoints:")
for endpoint in endpoints:
    # Simulate random response (normally would make real API call)
    actual_status = random.choice([200, 404, 500])

    if actual_status == endpoint["expected_status"]:
        print(f"PASS - {endpoint['url']} returned {actual_status}")
        passed += 1
    else:
        print(f"FAIL - {endpoint['url']} expected {endpoint['expected_status']}, got {actual_status}")
        failed += 1

print(f"\nTest Results: {passed} passed, {failed} failed")

print("\n✅ Day 2 Loops Exercise Complete!")
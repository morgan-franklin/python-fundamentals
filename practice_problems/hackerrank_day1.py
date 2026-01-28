"""
HackerRank - Day 1 Practice Problems
"""


# Problem 1: Say "Hello, World!" With Python
# https://www.hackerrank.com/challenges/py-hello-world/problem

print("Hello, World!")


# Problem 2: Python If-Else
# https://www.hackerrank.com/challenges/py-if-else/problem
def even_odd(n):
    if n % 2 == 1:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

# Test
print("=== Even Odd ===")
even_odd(5)
even_odd(10)
even_odd(20)
even_odd(30)
even_odd(2)

# Problem 2: Arithmetic Operators
# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
def arithmetic(num1, num2):
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)

# Test
print("=== Arithmetic ===")
print("Test 5 & 10")
arithmetic(5, 10)

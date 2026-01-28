"""
HackerRank - Day 2 Practice Problems
"""


# Problem 1: Loops
# https://www.hackerrank.com/challenges/python-loops

def print_squares(n):
    """Print squares of numbers 0 to n-1"""
    for numbers in range(n):
        print(numbers*numbers)


# Test
print("=== Squares ===")
print_squares(5)


# Problem 2: Print Function
# https://www.hackerrank.com/challenges/python-print

def print_numbers(n):
    """Print numbers 1 to n without newlines"""
    for numbers in range(1, n + 1):
        print(numbers, end="")
    print()  # New line at end


# Test
print("\n=== Print Numbers ===")
print_numbers(5)


# Problem 3: Runner-Up Score
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

def runner_up(scores):
    """Find second highest score"""
    # Remove duplicates and sort
    unique_scores = list(set(scores))
    unique_scores.sort(reverse=True)

    if len(unique_scores) >= 2:
        return unique_scores[1]
    return None


# Test
print("\n=== Runner-Up Score ===")
scores = [57, 57, 85, 100, 100, 45]
print(f"Scores: {scores}")
print(f"Runner-up: {runner_up(scores)}")


# Problem 4: FizzBuzz (LeetCode)
# https://leetcode.com/problems/fizz-buzz/

def fizz_buzz(n):
    """Return FizzBuzz list for 1 to n"""
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


# Test
print("\n=== FizzBuzz ===")
print(fizz_buzz(15))
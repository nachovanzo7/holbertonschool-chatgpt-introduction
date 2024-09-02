#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Args:
        n (int): The number for which the factorial is to be calculated.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the number from command line arguments
f = factorial(int(sys.argv[1]))
# Print the result
print(f)

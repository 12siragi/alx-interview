#!/usr/bin/python3
"""
Module that calculates the minimum number of operations needed
to get exactly n H characters in the file.
"""

def minOperations(n):
    """Returns the fewest number of operations needed to result in exactly n H characters."""
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations

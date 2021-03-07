"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
import math
from typing import Sequence


def is_fibonacci(n: int) -> bool:
    """
    Checks a single number is it a Fib number
    Look the original code and the explanation at stackoverflow
    https://stackoverflow.com/questions/7472128/check-input-that-belong-to-fibonacci-numbers-in-python
    Args:
        n: int number to be checked is it a fib number

    Returns: True if n is a fibonacci number, False otherwise

    """
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n
    return n == 0 or abs(round(a) - a) < 1.0 / n


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    Checks a sequence is it a fib sequence
    The length of Sequence is required to be >= 3 and shouldn't start from 0.
    Args:
        data: a sequence of int numbers

    Returns: True if given sequence is a fib numbers, False otherwise

    """
    if len(data) < 3 or 0 in data:
        return False

    for i in data:
        if not is_fibonacci(i):
            return False

    for j in range(len(data) - 2):
        if data[j] > data[j + 1]:
            return False

    return True

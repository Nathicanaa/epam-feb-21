"""
Here's a not very efficient calculation function that calculates something important:


Calculate total sum of slow_calculate() of all numbers starting from 0 to 500. Calculation time should not take
more than a minute. Use functional capabilities of multiprocessing module.
 You are not allowed to modify slow_calculate function
"""
import hashlib
import random
import struct
import time
from multiprocessing import Pool
from typing import Iterable


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def fast_calculate(numbers: Iterable[int]):
    """
    Takes iterable ints and returns total sum of slow_calculate() by modifying initial
    function with multiprocessing module benefits
    Args:
        numbers: iterable ints

    Returns: total sum of slow_calculate() of all numbers

    """
    with Pool(processes=60) as pool:
        return sum(pool.map(slow_calculate, numbers))

# # this code probably contain bugs...
#
#
# def _check_window(x: int, y: int, z: int) -> bool:
#     return (x + y) == z
#
#
# data_to_process = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
#
#
# assert len(data_to_process) >= 3
#
# a, b, c = data_to_process[0], data_to_process[1], data_to_process[2]
#
# while data_to_process:
#     if not _check_window(a, b, c):
#         raise ValueError("Invalid data")
#
#     a, b, c = b, c, data_to_process[0]
#     data_to_process = data_to_process[1:]
#
# print("it's a fib sequence!")
"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence  # here was 'collections' instead of 'typing'

#  This function returns True if the given Sequence is a Fib numbers, otherwise it returns False.
#  The length of Sequence is required to be > 0.


def check_fibonacci(data: Sequence[int]) -> bool:
    for i in range(len(data)):
        if i < 2:
            if i == data[i]:
                continue
            return False
        if data[i] != data[i - 2] + data[i - 1]:
            return False

    return True


data_to_process = [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
]
print(check_fibonacci(data_to_process))

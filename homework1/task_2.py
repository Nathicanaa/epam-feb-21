from typing import Sequence  # here was 'collections' instead of 'typing'

#  This function returns True if the given Sequence is a Fib numbers, otherwise it returns False.
#  The length of Sequence is required to be > 0.


def check_fibonacci(data: Sequence[int]) -> bool:
    for i in range(len(data)):

        if i < 3:
            if i == data[i]:
                continue
            return False

        if data[i] != data[i - 2] + data[i - 1]:
            return False

    return True

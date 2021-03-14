"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator


def fizzbuzz(n: int) -> Generator:
    """
    Take a number N and yields N FuzzBuzz number
    if n is not int TypeError will be raised
    Args:
        n: some int number

    Returns: generator object for fizzbuzz nums from 1 to N

    """
    try:
        for i in range(1, n + 1):
            yield "Fizz" * (i % 3 < 1) + (i % 5 < 1) * "Buzz" or str(i)
    except TypeError:
        raise TypeError("N must be an integer!")

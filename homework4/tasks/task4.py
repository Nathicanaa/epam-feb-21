"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.
That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions
>> fizzbuzz(5)
["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Take a number N and returns N FuzzBuzz number
    if n is not int TypeError will be raised
    Args:
        n: some int number

    Returns: list of fizzbuzz nums from 1 to N

    - Install Python 3.8 (https://www.python.org/downloads/)
    - Install pytest `pip install pytest`
    - Clone the repository https://github.com/Nathicanaa/epam-feb-21.git
    - Checkout branch homework4
    - Open terminal
    - run python -m doctest -v task4.py

    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']

    >>> fizzbuzz(1.5)
    Traceback (most recent call last):
        ...
    ValueError: N must be an integer!

    >>> fizzbuzz('data')
    Traceback (most recent call last):
        ...
    ValueError: N must be an integer!
    """
    if not isinstance(n, int):
        raise TypeError(f"N {n} must be an integer!")

    fuzz_lst = []
    for i in range(1, n + 1):
        if not i % 15:
            fuzz_lst.append("FizzBuzz")
        elif i % 3 == 0:
            fuzz_lst.append("Fizz")
        elif i % 5 == 0:
            fuzz_lst.append("Buzz")
        else:
            fuzz_lst.append(str(i))
    return fuzz_lst


if __name__ == "__main__":
    import doctest

    doctest.testmod()

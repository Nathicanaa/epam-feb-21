"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """
    data in a file should be line-delimited integers
    Args:
        file_name: name or path of a file, str type

    Returns: a tuple with int min and max values of the file

    """
    min_value = max_value = None
    with open(file_name, "r+", encoding="utf-8") as fi:

        for line in fi:
            x = int(line)

            if min_value is None:
                min_value = max_value = x

            elif x > max_value:
                max_value = x

            elif x < min_value:
                min_value = x

    return min_value, max_value

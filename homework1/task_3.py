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
    min_value = 0
    max_value = 0
    with open(file_name, "r", encoding="utf-8") as fi:
        for line in fi:
            x = int(line)

            if x > max_value:
                max_value = x

            elif x < min_value:
                min_value = x
    return min_value, max_value


# Alternative solution with readlines instead of line by line reading
# If guaranteed that the file contains line-delimited integers then we can use readlines method
# with map and list and then just return min and max of a list
# def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
#      with open(file_name, "r", encoding="utf-8") as fi:
#          x = list(map(int, fi.readlines()))
#          return min(x), max(x)

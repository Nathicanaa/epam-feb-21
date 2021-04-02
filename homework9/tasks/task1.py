"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import heapq
from pathlib import Path
from typing import Generator, Iterator, List, Union


def get_yield_from_file(file: Union[Path, str]) -> Generator:
    """
    Takes a file and yields element by element integers from the file
    According to task description file containing sorted array of ints
    Args:
        file: a path to the file in str or pathlib.Path

    Yields: int element of file one by one

    """
    with open(file, encoding="utf-8") as f:
        for line in f:
            yield int(line.strip())


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """
    A function to merge k sorted arrays taken from file list.
    Uses heapq.merge.
    Returns an iterator over the sorted values
    Args:
        file_list: collection of files containing sorted arrays

    Returns: result of sorting arrays

    """
    return heapq.merge(*[get_yield_from_file(file) for file in file_list])

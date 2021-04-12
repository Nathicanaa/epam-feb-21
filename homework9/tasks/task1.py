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


class SortingError(Exception):
    """Exception to be raised if an array is not sorted"""

    pass


def check_sorting(array: List) -> bool:
    """
    Checks list for sorting
    Args:
        array: some list
    Returns: true if list is sorted otherwise false
    """
    return array == sorted(array)


def check_path(path: Union[str, Path]) -> bool:
    """
    Checks path for being an instance of Path class and after that
    checks for existing and being a file
    If path not a Path instance then func converts it to Path type
    and checks for the same states as above
    Args:
        path: str path or Path instance
    Returns: true if path is a file and exists
    """
    if isinstance(path, Path):
        return path.exists() and path.is_file()

    return Path(path).is_file() and Path(path).exists()


def check_integers(file: Union[str, Path]) -> bool:
    """
    Checks file for containing only integer numbers
    Args:
        file: str path or Path instance
    Returns: true if file contains only integers otherwise false
    """
    with open(file, encoding="utf-8") as f:
        return all(line.strip().isdigit() for line in f)


def get_yield_from_file(path: Union[Path, str]) -> Generator:
    """
    Takes a file and yields element by element integers from the file
    if file exists and containing integers only
    Args:
        path: a path to the file in str or pathlib.Path
    Raises:
        TypeError if file doesn't exist or path to this path is incorrect
        ValueError if file doesn't contain integers only
    Yields: int element of file one by one
    """
    if not check_path(path):
        raise TypeError(f"path {path} is incorrect or searched file doesn't exist!")

    if not check_integers(path):
        raise ValueError(f"The file {path} doesn't contain integers only!")

    with open(path, encoding="utf-8") as f:
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
    for el in file_list:
        if not check_sorting(list(get_yield_from_file(el))):
            raise SortingError(f"File {el} has unsorted array!")

    return heapq.merge(*[get_yield_from_file(file) for file in file_list])

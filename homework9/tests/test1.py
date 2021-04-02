# A test for homework9 task1
from itertools import chain
from random import randint
from tempfile import NamedTemporaryFile

import pytest

from homework9.tasks.task1 import merge_sorted_files


@pytest.mark.parametrize(
    "data1, data2, expected_result",
    [
        ("1\n3\n5\n", "2\n4\n6\n", [1, 2, 3, 4, 5, 6]),
        ("10\n10\n20\n", "10\n15\n25\n", [10, 10, 10, 15, 20, 25]),
        ("0\n1\n", "0\n3\n", [0, 0, 1, 3]),
    ],
)
def test_merge_sorted_files(data1, data2, expected_result):
    """
    Passes if merge_sorted_files merges 2 sorted arrays correctly
    """
    with NamedTemporaryFile(mode="w+", delete=False) as file1:
        file1.write(data1)
        file1.seek(0)
    with NamedTemporaryFile(mode="w+", delete=False) as file2:
        file2.write(data2)
        file2.seek(0)
    assert list(merge_sorted_files([file1.name, file2.name])) == expected_result


def test_merge_sorting_many_arrays():
    """
    Passes if merging many sorted arrays from different files works correctly
    creating a list with sorted lists of integers, then writing every nested list in a temp files
    and after that merge_sorted_files takes these files as args and comparing to
    sorted(irertools.chain(*iterables)) which should return the same result
    """
    list_of_lists = [sorted([randint(1, 50) for _ in range(10)]) for _ in range(5)]
    with NamedTemporaryFile(mode="w+", delete=False) as file1:
        file1.write("".join([str(i) + "\n" for i in list_of_lists[0]]))
        file1.seek(0)
    with NamedTemporaryFile(mode="w+", delete=False) as file2:
        file2.write("".join([str(i) + "\n" for i in list_of_lists[1]]))
        file2.seek(0)
    with NamedTemporaryFile(mode="w+", delete=False) as file3:
        file3.write("".join([str(i) + "\n" for i in list_of_lists[2]]))
        file3.seek(0)
    with NamedTemporaryFile(mode="w+", delete=False) as file4:
        file4.write("".join([str(i) + "\n" for i in list_of_lists[3]]))
        file4.seek(0)
    with NamedTemporaryFile(mode="w+", delete=False) as file5:
        file5.write("".join([str(i) + "\n" for i in list_of_lists[4]]))
        file5.seek(0)
    assert list(
        merge_sorted_files([file1.name, file2.name, file3.name, file4.name, file5.name])
    ) == sorted(chain(*list_of_lists))

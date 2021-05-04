# A test for find_maximal_subarray_sum fun from homework1_Base_topics.task_5
from typing import List

import pytest

from homework1_Base_topics.Tasks.task_5 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["array", "length", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([], 3, 0),
        ([1, 3, -1, -3, 5, 3, 6, 7], 0, 0),
        ([-11, -3, -1, -3, 5, 3, 6, -7], 3, 14),
        ([-1, 3, -1, -3, 5, -3, 6, 7], 2, 13),
        ([-1, -1, -1, -3, -5, -3, -6, -7], 3, -1),
        ([-1, -1, 4], 1, 4),
        ([-1, -2, -3], 3, -1),
        ([-1, 0, -1, 0, -1, 1], 3, 1),
        ([-1, -1, -1, -3, -5, -3, -6, 1], 5, 1),
        ([], 0, 0),
    ],
)
def test_find_maximal_subarray_sum(array: List[int], length: int, expected_result: int):
    """Passes the test if find_maximal_subarray_sum with the given array
    and length og a subarray is equal to expected_result"""
    assert find_maximal_subarray_sum(array, length) == expected_result

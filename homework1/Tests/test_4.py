# A test for check_sum_of_four func from homework1.Tasks.task_4

from typing import List

import pytest

from homework1.Tasks.task_4 import check_sum_of_four


@pytest.mark.parametrize(
    ["a_list", "b_list", "c_list", "d_list", "expected_result"],
    [
        ([-1, -1], [-1, -1], [-1, -1], [-1, -1], 0),
        ([], [], [], [], 0),
        ([1], [1], [1], [1], 0),
        ([-1, -1, -1], [-1, -1, -1], [1, 1, 1], [1, 1, 1], 81),
        ([-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], 0),
        ([1, 2], [-2, -1], [-1, 2], [0, 2], 2),
    ],
)
def test_check_sum_of_four(
    a_list: List[int],
    b_list: List[int],
    c_list: List[int],
    d_list: List[int],
    expected_result: int,
):
    """Passes if check_sum_of_four with args is equal to expected_result"""
    assert check_sum_of_four(a_list, b_list, c_list, d_list) == expected_result

# A test for check_fibonacci func from task 2
from typing import Sequence

import pytest

from homework1.Tasks.task_2 import check_fibonacci


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ([0], False),
        ([0, 1], False),
        ([1, 1], False),
        ([-1, -2, -3], False),
        ([0, 1, 1, 2, 3, 5, 8, 13], False),
        ([3, 5], False),
        ([5, 3, 8], False),
        ([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144], True),
        ([514229, 832040, 1346269], True),
        ([4, 5, 9], False),
        ([1, 1, 2], True),
        (
            [
                21,
                34,
                55,
                89,
                144,
                233,
                377,
                610,
                987,
                1597,
                2584,
                4181,
                6765,
                10946,
                17711,
            ],
            True,
        ),
    ],
)
def test_check_fibonacci(data: Sequence[int], expected_result: bool):
    """
    Passes test if `check_fibonacci`(`data`)
    is equal to `expected_result`.
    """
    assert check_fibonacci(data) == expected_result

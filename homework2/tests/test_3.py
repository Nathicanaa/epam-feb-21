# A test for task3 from homework1


from typing import Any, List

import pytest

from homework2.tasks.task_3 import combinations


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ([[1, 2], [3, 4]], [[1, 3], [1, 4], [2, 3], [2, 4]]),
        ([[1], [2], [3]], [[1, 2, 3]]),
        ([[1], [], [3]], []),
        (
            [[1, 2, 3, 4, 5, 6], [8, 9]],
            [
                [1, 8],
                [1, 9],
                [2, 8],
                [2, 9],
                [3, 8],
                [3, 9],
                [4, 8],
                [4, 9],
                [5, 8],
                [5, 9],
                [6, 8],
                [6, 9],
            ],
        ),
        ([[0, 0, 0], [1]], [[0, 1], [0, 1], [0, 1]]),
    ],
)
def test_combinations(data: List[Any], expected_result: List[list]):
    """Passes if combinations(data) is equal to expected_result"""
    assert combinations(*data) == expected_result

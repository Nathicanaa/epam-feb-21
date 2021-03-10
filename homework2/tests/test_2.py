# A test for task2 from homework1

from typing import List, Tuple

import pytest

from homework2.tasks.task_2 import major_and_minor_elem


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
    ],
)
def test_major_and_minor_elem(data: List[int], expected_result: Tuple[int, int]):
    """Passes if major_and_minor_elem(inp) is equal to expected_result"""
    assert major_and_minor_elem(data) == expected_result


@pytest.mark.parametrize(
    ["data", "expected_result", "error_message"],
    [
        ([1, 2], ValueError, "There is no least common element"),
        (
            [
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            ValueError,
            "There is no least common element",
        ),
        ([10, 10, 10, 3, 3, 3, 4, 5], ValueError, "There is no least common element"),
        (
            [10, 10, 10, 10, 10, 10, 3, 3, 3, 4, 5],
            ValueError,
            "There is no least common element",
        ),
    ],
)
def test_error_case_major_and_minor_elem(
    data: List[int], expected_result: Exception, error_message: str
):
    """Passes if major_and_minor_elem(inp) is equal to expected_result"""
    with pytest.raises(expected_result) as exc:
        major_and_minor_elem(data)
    assert str(exc.value) == error_message

# A test for homework3_functional_programming task_4
import pytest

from homework3_functional_programming.tasks.task_4 import is_armstrong


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [(1, True), (9, True), (10, False), (153, True), (92727, True)],
)
def test_is_armstrong(number: int, expected_result: bool):
    """
    passes if is_armstrong(number) is equal to expected_result
    """
    assert is_armstrong(number) == expected_result

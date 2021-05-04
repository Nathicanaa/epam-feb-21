# A test for homework 4 task 5
from typing import List

import pytest

from homework4_test_and_debugging.tasks.task5 import fizzbuzz


@pytest.mark.parametrize(
    "data,  expected_result",
    [
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (
            15,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        ),
        (0, []),
        (-1, []),
    ],
)
def test_fizzbuzz(data: int, expected_result: List[str]):
    """passes if fizzbuzz(data) is equal to expected result"""
    assert list(fizzbuzz(data)) == expected_result


@pytest.mark.parametrize(
    "data, expected_exception", [(1.6, TypeError), ("data", TypeError)]
)
def test_fizzbuzz_error(data: str, expected_exception: Exception):
    """
    Passes if fizzbuzz raises TypeError
    """
    with pytest.raises(TypeError, match=f"N {data} must be an integer!"):
        list(fizzbuzz(data))

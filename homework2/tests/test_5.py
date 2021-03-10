# A unit test for task5 from homework2

import string
from typing import Any, Iterable, List

import pytest

from homework2.tasks.task_5 import custom_range


@pytest.mark.parametrize(
    ["some_seq", "args", "expected_result"],
    [
        (string.ascii_lowercase, "g", ["a", "b", "c", "d", "e", "f"]),
        (
            string.ascii_lowercase,
            ("g", "p"),
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        (string.ascii_lowercase, ("p", "g", -2), ["p", "n", "l", "j", "h"]),
        ("qwerty", "y", ["q", "w", "e", "r", "t"]),
        ("qwerty", ("y", "q", -1), ["y", "t", "r", "e", "w"]),
        ("0123456789", ("0", "9", 2), ["0", "2", "4", "6", "8"]),
    ],
)
def test_custom_range(some_seq: Iterable[Any], args: Any, expected_result: List[Any]):
    """Passes test if custom_range(some_seq, *args) is equal to expected_result"""
    assert custom_range(some_seq, *args) == expected_result

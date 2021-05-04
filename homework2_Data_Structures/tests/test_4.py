# A unit test for task_4 from homework2_Data_Structures

from typing import Any, Callable, Tuple

import pytest

from homework2_Data_Structures.tasks.task_4 import cache


@pytest.mark.parametrize(
    ["function", "args"],
    [
        (lambda a, b: (a ** b) ** 2, (10, 10)),
        (lambda a, b: a + b + 1, (10, 10)),
        (lambda a, b: (a.upper, b.upper), ("moscow", "london")),
    ],
)
def test_cached(function: Callable, args: Tuple[Any]):
    """passes test if cached objects are equal( x is y )"""
    cached = cache(function)
    assert cached(*args) is cached(*args)

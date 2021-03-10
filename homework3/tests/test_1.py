# A test fort homework3 task1

from typing import Any, Callable, Tuple

import pytest

from homework3.tasks.task_1 import cache


@pytest.mark.parametrize(
    ["function", "args"],
    [
        (lambda a, b: (a ** b) ** 2, (10, 10)),
        (lambda a, b: a + b + 1, (10, 10)),
        (lambda a, b: (a.upper, b.upper), ("moscow", "london")),
    ],
)
def test_cached(function: Callable, args: Tuple[Any]):
    """passes test if cached objects are equal( x == y ),
    this test if from homework2"""

    @cache(times=2)
    def some(func):
        return func

    cached = some(function)
    assert cached(*args) == cached(*args)


def test_times_cache_decor():
    """
    passes if decorator with times param works correctly
    """

    @cache(times=2)
    def cheching_times():
        return x

    x = 0
    zero = cheching_times()

    x = 1
    first = cheching_times()

    x = 2
    second = cheching_times()

    x = 3
    third = cheching_times()

    assert zero == first == second
    assert second != third


@cache(times=2)
def f(a: int):
    return a * a


def test_cache_decorator_error():
    with pytest.raises(TypeError):
        assert f(3) is f() is f() is f()

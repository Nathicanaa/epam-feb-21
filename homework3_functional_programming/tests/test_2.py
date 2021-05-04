# A test for homework3_functional_programming task_02

from typing import Iterable

import pytest

from homework3_functional_programming.tasks.task_2 import fast_calculate, slow_calculate


@pytest.mark.parametrize("some_iter", [(range(5)), (range(1)), (range(0))])
def test_general_calculating_stability(some_iter: Iterable[int]):
    """passes test if general calculating logic is stable for both functions"""
    assert sum(slow_calculate(x) for x in some_iter) == fast_calculate(some_iter)


@pytest.mark.timeout(timeout=60)
def test_time_fast_calculate():
    """
    Passes if fast_calculate(range(500)) works less time than in timeout=
    """
    assert fast_calculate(range(500)) == 1024259

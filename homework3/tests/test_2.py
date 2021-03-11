# A test for homework3 task_02

from typing import Iterable

import pytest

from homework3.tasks.task_2 import fast_calculate, slow_calculate


@pytest.mark.parametrize("some_iter", [(range(5)), (range(1)), (range(0))])
def test_general_calculating_stability(some_iter: Iterable[int]):
    """passes test if general calculating logic is stable for both functions"""
    assert sum(slow_calculate(x) for x in some_iter) == fast_calculate(some_iter)

# A test fort homework3 task1

from unittest import mock

import pytest

from homework3.tasks.task_1 import cache


def test_times_cache_decor():
    """
    passes if decorator with times param works correctly
    """

    @cache(times=2)
    def checking_times():
        return x

    x = 0
    zero = checking_times()

    x = 1
    first = checking_times()

    x = 2
    second = checking_times()

    x = 3
    third = checking_times()

    assert zero is first is second
    assert second is not third


def test_value_error_for_cache():
    """
    Passes if raises ValueError with times < 1
    """
    with pytest.raises(ValueError) as exc:

        @cache(times=-1)
        def some(x):
            return x

        some("some")

    assert str(exc.value) == "Times must be equal at least to 1"

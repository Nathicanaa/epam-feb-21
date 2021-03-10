# A test for homework3 task_3
from typing import Callable, Tuple

import pytest

from homework3.tasks.task_3 import Filter, make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


@pytest.mark.parametrize(
    ["funcs", "expected_result", "error_message"],
    [
        (
            (lambda x, y: x + y, lambda z, v: z - v),
            ValueError,
            "Filter accepts only single-argument functions",
        ),
    ],
)
def test_error_call(
    funcs: Tuple[Callable], expected_result: Exception, error_message: str
):
    """
    Passes if exception was raised
    """
    with pytest.raises(expected_result) as exc:
        Filter(*funcs)
    assert str(exc.value) == error_message


def test_Filter():
    """
    Passes if we get correct result
    """
    positive_even = Filter(
        lambda a: a % 2 == 0, lambda a: a >= 0, lambda a: isinstance(a, int)
    )
    assert positive_even.apply(range(100)) == [x for x in range(99) if x % 2 == 0]


def test_make_filter():
    """
    Passes if make_filter works correctly
    """
    assert make_filter(name="polly", type="bird").apply(sample_data) == [sample_data[1]]


def test_make_filter2():
    """
    Passes if make_filter works correctly
    """
    assert make_filter(name="Bill", type="person").apply(sample_data) == [
        sample_data[0]
    ]

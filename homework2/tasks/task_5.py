"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


from typing import Any, Iterable, List


def custom_range(
    some_iter: Iterable[Any], start: Any, end: Any = None, step: int = 1
) -> List[Any]:
    """
    Make some_iter objects behave like range object
    Args:
        some_iter: some iterable object
        start: starting point
        end: ending point
        step: literally step in range func

    Returns: some_iter with range behavior

    """
    if not some_iter:
        return []

    if len(some_iter) != len(set(some_iter)):
        raise ValueError("Elements of object are not unique!")

    data = list(some_iter)

    if end is None:
        end = data.index(start)
        start = 0
    else:
        start = data.index(start)
        end = data.index(end)

    return data[start:end:step]

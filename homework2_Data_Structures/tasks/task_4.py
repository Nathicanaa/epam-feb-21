"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from typing import Any, Callable


def cache(function: Callable) -> Callable:
    """
    Takes a function and return the cached function as a result
    if args were called before return result from cache
    Args:
        function: a function what does something

    Returns: cached function

    """
    cached = {}

    def wrap(*args: Any) -> Any:
        """
        takes args and returns cache
        Args:
            *args: any arguments

        Returns: cached data

        """
        if args in cached:
            return cached[args]

        cached[args] = function(*args)

        return cached[args]

    return wrap

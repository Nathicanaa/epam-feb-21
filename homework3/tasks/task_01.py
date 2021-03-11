"""
In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

>> f()
? 1
'1'
>> f()     # will remember previous value
'1'
>> f()     # but use it up to two times only
'1'
>> f()
? 2
'2'
"""
from typing import Any, Callable


def cache(times: int = 3) -> Callable:
    """
    Modifying caching function with a param
    Args:
        times: int count of times giving cache out

    Returns: parametrized decorator

    """
    cached = {}
    timing = times
    if timing < 1:
        raise ValueError("Times must equals at least to 1 ")

    def decor(function: Callable):
        """
        A body of decorator
        Args:
            function: some function to be decorated

        Returns: decorated func

        """

        def wrap(*args: Any, **kwargs: Any):
            """
            Takes args and kwargs to return cached data, count times of
            giving cache out
            Args:
                *args: pos args
                **kwargs: key args

            Returns: cached data

            """
            spell = str(*args, **kwargs)
            nonlocal timing

            if spell in cached:
                data = cached[spell]

                if timing == 1:
                    del cached[spell]
                timing -= 1
                return data

            data = function(*args, **kwargs)
            timing = times
            cached[spell] = data
            return data

        return wrap

    return decor

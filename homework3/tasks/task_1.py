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


def cache(times: int) -> Callable:
    """
    Modifying caching function with a param
    Args:

        times: int count of times giving cache out

    Returns: parametrized decorator
    """
    if times < 1:
        raise ValueError("Times must be equal at least to 1")

    def decorate(function: Callable) -> Callable:
        """
        A body of decorator
        Args:
            function: some function to be decorated
        Returns: decorated func
        """
        cached = {}
        time_count = times

        def wrap(*args: Any) -> Any:
            """
            Takes args to return cached data, count times of
            giving cache out
            Args:

                *args: pos args

            Returns: cached data
            """
            nonlocal time_count
            if args in cached and time_count:
                time_count -= 1
                return cached[args]

            time_count = times
            cached[args] = function(*args)

            return cached[args]

        return wrap

    return decorate

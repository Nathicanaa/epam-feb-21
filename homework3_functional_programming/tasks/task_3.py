"""
# I decided to write a code that generates data filtering object from a list of keyword parameters:

# example of usage:
# positive_even = Filter(lamba a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(int, a)))
# positive_even.apply(range(100)) should return only even numbers from 0 to 99

# make_filter(name='polly', type='bird').apply(sample_data) should return only second entry from the list

# There are multiple bugs in this code. Find them all and write tests for faulty cases.

See the original code at
https://github.com/cdeler/epam_python_autumn_2020/blob/main/lecture_03_functional_programming/hw/task03/task03.py
"""
import inspect
from typing import Any, Callable, Dict, List, Tuple


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *functions: Callable):
        self.functions = self.check_single(functions)

    def apply(self, data: List[Any]) -> List[Any]:
        """
        Apply data
        Args:
            data: some input data

        Returns: checked data

        """
        return [
            item
            for item in data
            if all(check_single(item) for check_single in self.functions)
        ]

    @staticmethod
    def check_single(funcs: Tuple[Callable]):
        """
        check if funcs are single argument
        Returns: funcs they are single-argument type
        """
        for function in funcs:
            if len(inspect.signature(function).parameters) != 1:
                raise ValueError("Filter accepts only single-argument functions")

        return funcs


def make_filter(**keywords: Dict[Any, Any]) -> List[Any]:
    """
    Generate filter object for specified keywords
    Args:
        **keywords: keyword data

    Returns: Filter object

    """
    filter_funcs = [
        lambda x: x[key] == value if key in x else False
        for key, value in keywords.items()
    ]
    return Filter(*filter_funcs)

# A test for homework5_OOP_1 task2
import functools
from typing import Any

from homework5_OOP_1.tasks.task2 import print_result


@print_result
def custom_sum(*args: Any) -> Any:
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


def test_name():
    """
    Passes if __name__ of wrapped custom_sum is equal to custom_sum.__name__ without wrapper
    """
    assert custom_sum.__name__ == "custom_sum"


def test_doc():
    """
    Passes if __doc__ of wrapped custom_sum is equal to custom_sum.__doc__ without wrapper
    """
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"


def test_attr_after_wrap():
    """
    Passes if wrapped custom_sum has a new attribute "__original_sum"
    """
    assert hasattr(custom_sum, "__original_func") is True


def test_custom_sum_out_with_wrapper(capsys):
    """
    Passes if wrapped custom_sum works correctly and prints returned result in stdout
    """
    custom_sum([1, 2, 3], [4, 5])
    captured = capsys.readouterr()
    assert captured.out, captured.err == "[1, 2, 3, 4, 5]\n"


def test_custom_sum_out(capsys):
    """
    Passes if __original_func attr works correctly and don't prints result in stdout
    """
    custom_sum.__original_func([1, 2, 3], [4, 5])
    captured = capsys.readouterr()
    assert captured.out == ""

"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func
print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий
До применения вашего декоратор будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция
Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""

import functools
from typing import Any, Callable


def my_decorator(wrapped: Callable) -> Callable:
    """
    Takes wrapped funcs and returns it modified
    Based on functools.wraps decorator and has the same functionality
    Modifying __dict__ with new method __original_func which returns original behavior of wrapped
    Args:
        wrapped: function to be wrapped

    Returns: wrapped function

    """
    wrapped.__dict__["__original_func"] = wrapped
    return functools.wraps(wrapped)


def print_result(func: Callable) -> Callable:
    @my_decorator(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args: Any) -> Any:
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)

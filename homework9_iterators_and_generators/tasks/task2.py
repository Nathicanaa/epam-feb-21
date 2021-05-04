"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>with suppressor(IndexError):
...    [][2]
"""
import contextlib
from typing import Generator


class Suppressor:
    """
    A class for custom context manager to suppress passed exceptions
    Contains dunders:
        __init__
        __enter__
        __exit__
    """

    def __init__(self, exception: Exception):
        """
        Constructor magic method method
            exception: passed exception
        """
        self._exception = exception

    def __enter__(self):
        """
        Entering point in a context manager
        """
        pass

    def __exit__(self, _type: Exception, *args) -> bool:
        """
        Escaping point of a context manager
        If passed exception is correct then it will be suppressed, otherwise
        real exception will be raised
        For example:
            with Suppressor(NameError):
                print(name)   -  will be suppressed
            with Suppressor(KeyError):
                print(name)    - will raise NameError
        Args:
            _type: type of Exception
            *args: other __enters__ arguments that aren't needed for this case
        Returns: True if passed exception is a subclass for raised exception
        """
        return issubclass(_type, self._exception)


@contextlib.contextmanager
def suppressor(exception: Exception) -> Generator:
    """
    Context manager to suppress passed exceptions
    works same as the Suppressor class, but has func realization
    If passed exception is correct then it will be suppressed, otherwise
    real exception will be raised
    For example:
        with suppressor(NameError):
            print(name)   -  will be suppressed
        with suppressor(KeyError):
            print(name)    - will raise NameError
    Args:
        exception: passed Exception
    Returns: suppresses the exception
    """
    try:
        yield
    except exception:
        pass

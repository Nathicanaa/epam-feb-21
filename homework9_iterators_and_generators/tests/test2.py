# A test for Homework9 task 2
import pytest

from homework9_iterators_and_generators.tasks.task2 import Suppressor, suppressor


# Tests for the class
def test_supressor_class_name_positive_name_error(capsys):
    """
    Passes if NameError was suppressed
    """
    with Suppressor(NameError):
        print(name)
    captured = capsys.readouterr()
    assert captured.err == ""


def test_supressor_class_positive_index_error(capsys):
    """
    Passes if IndexError was suppressed
    """
    with Suppressor(IndexError):
        [][2]
    captured = capsys.readouterr()
    assert captured.err == ""


def test_supressor_class_negative_name_error():
    """
    Passes if NameError was raised
    """
    with pytest.raises(NameError):
        with Suppressor(KeyError):
            print(name)


def test_supressor_class_negative_index_error():
    """
    Passes if IndexError was raised
    """
    with pytest.raises(IndexError):
        with Suppressor(KeyError):
            [][2]


# Tests for the func
def test_supressor_func_name_positive_name_error(capsys):
    """
    Passes if NameError was suppressed
    """
    with suppressor(NameError):
        print(name)
    captured = capsys.readouterr()
    assert captured.err == ""


def test_supressor_func_positive_index_error(capsys):
    """
    Passes if IndexError was suppressed
    """
    with suppressor(IndexError):
        [][2]
    captured = capsys.readouterr()
    assert captured.err == ""


def test_supressor_func_negative_name_error():
    """
    Passes if NameError was raised
    """
    with pytest.raises(NameError):
        with suppressor(KeyError):
            print(name)


def test_supressor_func_negative_index_error():
    """
    Passes if IndexError was raised
    """
    with pytest.raises(IndexError):
        with suppressor(KeyError):
            [][2]

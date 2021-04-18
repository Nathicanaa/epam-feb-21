# A test for homework11 task1
from enum import Enum

import pytest

from homework11.tasks.task1 import SimplifiedEnum


class ColorsEnumStandard(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class ColorsEnumSimplified(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


def test_getting_attrs():
    """
    Passes if getting attrs goes as expected
    """
    assert ColorsEnumStandard.BLUE.value is "BLUE"
    assert ColorsEnumSimplified.BLUE is "BLUE"
    assert ColorsEnumStandard.BLUE.value is ColorsEnumSimplified.BLUE


def test_len():
    """
    Passes if len returned and works for both classes as expected
    """
    assert len(ColorsEnumStandard) == len(ColorsEnumSimplified) == 4


def test_iter():
    """
    Passes if  iteration implemented and works for both classes in the same way
    """
    it = iter(ColorsEnumSimplified)
    it1 = iter(ColorsEnumStandard)
    assert next(it) is "RED"
    assert next(it1) is ColorsEnumStandard.RED


def test_ColorsEnumSimplified_error():
    """Passes if ValueError was raised"""
    with pytest.raises(AttributeError):
        ColorsEnumSimplified.RED.value

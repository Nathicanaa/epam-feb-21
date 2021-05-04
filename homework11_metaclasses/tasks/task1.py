"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""
from typing import Iterator, Tuple, TypeVar

SimplifiedEnum_child = TypeVar("SimplifiedEnum_child")


class SimplifiedEnum(type):
    def __new__(mcs, class_name: str, bases: Tuple, class_dict) -> SimplifiedEnum_child:
        """
        Makes new enum class
        Args:
            class_name: name of new enum class
            bases: the tuple of bases to be given to __new__
            class_dict: __dict__ of new class (namespace)
        """
        name = class_name
        class_dict = {key: key for key in class_dict[f"_{class_name}__keys"]}
        enum_class = super().__new__(mcs, class_name, bases, class_dict)
        enum_class.__keys = class_dict
        return enum_class

    def __iter__(self) -> Iterator:
        """
        Provides iteration through __keys
        Returns:
        """
        yield from self.__keys

    def __len__(self) -> int:
        """
        Dunder method to get len of __keys
        Returns: len of __keys
        """
        return len(self.__keys)

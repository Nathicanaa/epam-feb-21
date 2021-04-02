"""
We have a file that works as key-value storage, each like
is represented as key and value separated by = symbol, example:
name=kek last_name=top song_name=shadilay power=9001
Values can be strings or integer numbers. If a value can be treated both as a number
and a string, it is treated as number.
Write a wrapper class for this key value storage that works like this:
storage = KeyValueStorage('path_to_file.txt') that has its keys and values
accessible as collection items and as attributes.
Example: storage['name'] # will be string 'kek' storage.song_name
# will be 'shadilay' storage.power # will be integer 9001
In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute
(for example when there's a line 1=something) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""
from collections import defaultdict
from keyword import iskeyword
from typing import Dict, Optional


def check(line: str) -> bool:
    """
    Checks string for validity for be a key into a dict
    Args:
        line: some string
    Returns: true if line is valid false otherwise
    """
    return not iskeyword(line) and line.isidentifier()


class KeyValueStorage:
    """
    A class to work with a file containing pairs like key=value
    if a key is valid then pair (key, value) will be added to dct.
    Providing access to dict value through attributes and by dict[key] method
    """

    def __init__(self, path: str):
        """
        Constructor method, takes a path to a file containing pairs key,value
        as argument, reads this file and checks keys for validity
        if key is not valid, ValueError will be raised
        if value can be treated as an int it will be type casted to int
        finally adds pairs key,value into dct
        Args:
            path: a path to a file
        """
        self.dct = defaultdict(dict)
        with open(path, "r+", encoding="utf-8") as file:
            pairs = [pair.split("=") for pair in file.read().split()]
        for key, value in pairs:
            if not check(key):
                raise ValueError(f"The key {key} is not valid!")
            if key in dir(self):
                raise ValueError(f"The key {key} is clashing with built-in attr")
            if value.isdigit():
                value = int(value)
            self.dct[key] = value

    def __getattr__(self, key: str) -> Optional[Dict]:
        """
        Magic method returns attr if exists in dct
        otherwise raises AttributeError
        Args:
            key: any str key
        Returns: value for a key from dct
        Raises: AttributeError if key not in dct
        """
        if key not in self.dct:
            raise AttributeError(f"Attribute {key} doesn't exist!")
        return self.dct[key]

    def __getitem__(self, key: str) -> Optional[Dict]:
        """
        Magic method returns item by dict[key] syntax
        otherwise raises AttributeError
        Args:
            key: any str key
        Returns: value for a key from dct
        Raises: AttributeError if key not in dct
        """
        if key not in self.dct:
            raise AttributeError(f"Key {key} doesn't exist!")
        return self.dct[key]

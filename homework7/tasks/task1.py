"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool

from typing import Any


# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    ...


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """
    Takes a tree (dict) and an element to check occurrences of element
    in this tree. Recursively searches for an element in a tree and nested subtrees
    nested subtree can be basic collections ( list, tuple, set, dict ) or basic data
    types ( int, bool, str )
    Args:
        tree: some tree, according to task requirements it should be a dict,
        but actually nested subtrees can be any iterable ( look example_tree )
        element: an element to be found in the tree

    Returns: count of element's occurrences into the tree
    """
    counter = 0

    if tree == element:
        counter += 1

    if isinstance(tree, (list, set, tuple)):
        for i in tree:
            counter += find_occurrences(i, element)

    if isinstance(tree, dict):
        for key, value in tree.items():
            counter += find_occurrences(key, element)
            counter += find_occurrences(value, element)

    return counter

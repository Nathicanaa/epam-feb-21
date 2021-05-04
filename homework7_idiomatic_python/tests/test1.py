# A test for homework7_idiomatic_python task1

import pytest

from homework7_idiomatic_python.tasks.task1 import find_occurrences

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
        },
    },
    "fourth": "RED",
}
single_element_str = "RED"
single_element_dict = {"RED": "RED"}


@pytest.mark.parametrize(
    "data, element, expected_result",
    [
        (example_tree, "RED", 6),
        (example_tree, "first", 1),
        (example_tree, "key1", 1),
        (example_tree, "BLUE", 2),
        (example_tree, "doesn't exist", 0),
        (example_tree, 123, 0),
        (single_element_str, "RED", 1),
        (single_element_dict, "RED", 2),
    ],
)
def test_find_occurrences(data, element, expected_result):
    """
    Passes if find_occurrences(data, element) is equal to expected result
    """
    assert find_occurrences(data, element) == expected_result

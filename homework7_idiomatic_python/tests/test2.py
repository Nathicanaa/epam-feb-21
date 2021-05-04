# A test for homework7_idiomatic_python task2

import pytest

from homework7_idiomatic_python.tasks.task2 import backspace_compare


@pytest.mark.parametrize(
    "first_string, second_string, expected_result",
    [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("####", "#", True),
        ("", "", True),
        ("a#c", "b", False),
        ("a", "c", False),
        ("a##b##c##", "a##b##c##s", False),
    ],
)
def test_backspace_compare(first_string, second_string, expected_result):
    """
    Passes if backspace_compare(first_string, second_string) is equal to expected result
    """
    assert backspace_compare(first_string, second_string) == expected_result

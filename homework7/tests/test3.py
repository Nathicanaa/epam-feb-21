# A test for homework7 task3

import pytest

from homework7.tasks.task3 import tic_tac_toe_checker

example_1 = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]

example_2 = [["x", "x", "o"], ["o", "x", "o"], ["x", "o", "x"]]

example_3 = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "o"]]

example_4 = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

example_5 = [["o", "x", "o"], ["o", "x", "o"], ["x", "o", "x"]]

example_6 = [["x", "o", "x"], ["x", "o", "x"], ["o", "x", "o"]]


@pytest.mark.parametrize(
    "example, expected_result",
    [
        (example_1, "unfinished!"),
        (example_2, "x wins!"),
        (example_3, "o wins!"),
        (example_4, "unfinished!"),
        (example_5, "draw!"),
        (example_6, "draw!"),
    ],
)
def test_tic_tac_toe_checker(example, expected_result):
    """
    Passes if tic_tac_toe_checker(example) is equal to expected_result
    """
    assert tic_tac_toe_checker(example) == expected_result

# A test for homework4_test_and_debugging task 3

import pytest

from homework4_test_and_debugging.tasks.task3 import my_precious_logger


@pytest.mark.parametrize(
    "data, expected_out_result, expected_err_result",
    [
        ("some text", "some text\n", ""),
        ("error data", "", "error data\n"),
        ("", "\n", ""),
        (" ", " \n", ""),
        ("1", "1\n", ""),
    ],
)
def test_my_precious_logger(
    capsys, data: str, expected_out_result: str, expected_err_result: str
):
    """
    Passes my_precious_logger(data) outputs correctly
    Uses capsys fixture from pytest
    [https://docs.pytest.org/en/stable/capture.html]
    """
    my_precious_logger(data)
    captured = capsys.readouterr()
    assert captured.out == expected_out_result
    assert captured.err == expected_err_result

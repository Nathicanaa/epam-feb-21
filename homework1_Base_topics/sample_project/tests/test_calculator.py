# A test for calc module
import pytest

from homework1_Base_topics.sample_project.calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (65536, True),
        (12, False),
        (0, False),
        (-1, False),
        (2 ** 100, True),
        (2 ** 0, True),
    ],
)
def test_power_of_2(value: int, expected_result: bool):
    """
    Passes the test if check_power_of_2(value)'s result
    is equal to expected result
    """
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result

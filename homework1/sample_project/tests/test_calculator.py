# Added 0, -1, 2 ** 100, 2 ** -1 and 2 ** 0 to pytest.mark params
import pytest

from homework1.sample_project.calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (65536, True),
        (12, False),
        (0, False),
        (-1, False),
        (2 ** 100, True),
        (2 ** -1, True),
        (2 ** 0, True),
    ],
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result

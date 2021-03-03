# A test for task3 from homework1
from tempfile import NamedTemporaryFile
from typing import Tuple

import pytest

from homework1.Tasks.task_3 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ("0\n", (0, 0)),
        ("1\n2\n3\n4\n5\n", (1, 5)),
        ("-1\n-10\n1000\n0\n", (-10, 1000)),
        ("-1\n-2\n-3\n-100\n", (-100, -1)),
    ],
)
def test_find_maximum_and_minimum(data: str, expected_result: Tuple[int, int]):
    """
    Uses NamedTemporaryFile as a file with data
    if find_maximum_and_minimum(file.name) is equal to expected_result test is passed
    :param data: data to be written into temp file
    :param expected_result: result of find_maximum_and_minimum(file.name)
    """
    with NamedTemporaryFile(mode="w+", delete=False) as file:
        file.write(data)
        file.seek(0)
        assert find_maximum_and_minimum(file.name) == expected_result

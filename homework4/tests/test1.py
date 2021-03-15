# A test for homework4 task1
from tempfile import NamedTemporaryFile

import pytest

from homework4.tasks.task1 import read_magic_number

fake_path = r"C:\Users\Users\Users\Users\Users\Users\Users.txt"


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ("1\nmain\n3123123\nxx", True),
        ("2\n", True),
        ("1.5", True),
        ("3\n", False),
        ("0\n", False),
        ("10.5\n", False),
    ],
)
def test_read_magic_number(data: str, expected_result: bool):
    """
    Uses NamedTemporaryFile as a file with data
    if read_magic_number(file.name) is equal to expected_result test is passed
    """
    with NamedTemporaryFile(mode="w+", delete=False) as file:
        file.write(data)
        file.seek(0)
        assert read_magic_number(file.name) == expected_result


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ("data", ValueError),
        ("6u7u9i00", ValueError),
        ("===123sad==", ValueError),
    ],
)
def test_read_magic_number_no_numeric_data(data: str, expected_result: Exception):
    """
    Uses NamedTemporaryFile as a file with data
    if read_magic_number(file.name) is equal to expected_result test is passed
    """
    with NamedTemporaryFile(mode="w+", delete=False) as file:
        file.write(data)
        file.seek(0)
        with pytest.raises(expected_result, match=f"Data {data} has wrong format"):
            read_magic_number(file.name)


def test_read_magic_number_file_does_not_exist():
    with pytest.raises(ValueError, match="File doesn't exist!"):
        read_magic_number(fake_path)

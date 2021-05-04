# A test to homework4_test_and_debugging task2
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError

import pytest

from homework4_test_and_debugging.tasks.task2 import count_dots_on_i


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (b'<span class="pl-s"> - function is created</span>', 2),
        (b"iiiiiiiiii", 10),
        (b"qqwweeqwertyuasd", 0),
    ],
)
@patch("urllib.request.urlopen")
def test_count_dots_on_i(mock_urlopen, input_data: bytes, expected: int):
    """
    Patching urlopen for returning expected result
    Passes if count_dots_on_i(mock) is equal to expected result
    """
    my_mock = MagicMock(**{"read.return_value": input_data})
    mock_urlopen.return_value = my_mock
    call = count_dots_on_i(my_mock)
    assert call == expected


@patch("urllib.request.urlopen")
def test_negative_count_dots_on_i(mock_urlopen):
    """
    Uses urllib side_effect to raise error
    Passes if Value error was raised
    """
    my_mock1 = MagicMock()
    mock_urlopen.side_effect = HTTPError("http://mokc_url.su", 404, "Error", {}, None)
    with pytest.raises(ValueError):
        count_dots_on_i(my_mock1)

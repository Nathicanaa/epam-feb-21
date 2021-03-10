# A unit test to homework2 task_1

from typing import List

import pytest

from homework2.tasks.task_1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)

test_data = (
    r"C:\Users\Roman\PycharmProjects\epam-feb-21_new\homework2\tests\test_data.txt"
)


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (
            test_data,
            [
                "Souveränitätsansprüche",
                "unmißverständliche",
                "Bevölkerungsabschub",
                "symbolischsakramentale",
                "Kollektivschuldiger",
                "unverhältnismäßig",
                "Werkstättenlandschaft",
                "Schicksalsfiguren",
                "Selbstverständlich",
                "Verwaltungsmaßnahme",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(data: str, expected_result: List[str]):
    """passes test if get_longest_diverse_words(data) is equal to expected_result"""
    assert get_longest_diverse_words(data) == expected_result


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (test_data, "›"),
    ],
)
def test_get_rarest_char(data: str, expected_result: str):
    """Passes the test if get_rarest_char(data) is equal to expected result"""
    assert get_rarest_char(data) == expected_result


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (test_data, 5305),
    ],
)
def test_count_punctuation_chars(data: str, expected_result: int):
    """passes the test if count_punctuation_chars(data) is equal to expected result"""
    assert count_punctuation_chars(data) == expected_result


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (test_data, 2972),
    ],
)
def test_count_non_ascii_chars(data: str, expected_result: int):
    """passes the test if count_non_ascii_chars(data) is equal to expected result"""
    assert count_non_ascii_chars(data) == expected_result


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (test_data, "ä"),
    ],
)
def test_get_most_common_non_ascii_char(data: str, expected_result: str):
    """passes the test if get_most_common_non_ascii_char(data) is equal to expected result"""
    assert get_most_common_non_ascii_char(data) == expected_result

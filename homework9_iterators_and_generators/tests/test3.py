# A test for homework 9 task 3

import pytest

from homework9_iterators_and_generators.tasks.task3 import universal_file_counter


@pytest.mark.parametrize(
    "data1, data2, expected_result",
    [
        ("1\n2\n3\n4\n5\n6\n", "1\n2\n3\n4\n5\n6\n", 12),
        ("\n\n\n\n", "\n\n\n\n", 8),
        ("123s 5\n123879   \n ", "123s 5\n123879   \n ", 6),
        ("", "", 0),
        ("\n     \n main", "\n     \n main", 6),
    ],
)
def test_no_tokenize_counter(tmp_path, data1, data2, expected_result):
    """
    Creates temp directory and 2 temp files using tmp_path fixture
    writes into them same data
    Passes if universal_file_counter counting lines correctly in these files
    """
    directory = tmp_path / "sub"
    directory.mkdir()
    path_1 = directory / "no_token1.txt"
    path_2 = directory / "no_token2.txt"
    path_1.write_text(data1)
    path_2.write_text(data2)
    assert universal_file_counter(directory, "txt") == expected_result


@pytest.mark.parametrize(
    "data1, data2, expected_result",
    [
        ("1\n2\n3\n4\n5\n6\n", "1\n2\n3\n4\n5\n6\n", 12),
        ("\n\n\n\n", "\n\n\n\n", 0),
        ("123s 5\n123879   \n ", "123s 5\n123879   \n ", 6),
        ("", "", 0),
        ("\n     \n main", "\n     \n main", 2),
    ],
)
def test_with_tokenize_counter(tmp_path, data1, data2, expected_result):
    """
    Creates temp directory and 2 temp files using tmp_path fixture
    writes into them same data
    Passes if universal_file_counter counting tokens correctly in these files
    """
    directory = tmp_path / "sub"
    directory.mkdir()
    path_1 = directory / "token1.txt"
    path_2 = directory / "token2.txt"
    path_1.write_text(data1)
    path_2.write_text(data2)
    assert universal_file_counter(directory, "txt", str.split) == expected_result

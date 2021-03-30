# A test for homework8 task2
import pytest

from homework8.tasks.task2 import TableData

presidents = TableData("example.sqlite", table_name="presidents")
books = TableData("example.sqlite", table_name="books")


def test_len_tables():
    """
    Passes if len of tables is equal to their count of rows
    """
    assert len(presidents) == 3
    assert len(books) == 3


def test_get_by_key_presidents_positive():
    """
    Passes if TableData class provides an access to table rows through dict[key] syntax
    """
    assert presidents["Yeltsin"] == {"name": "Yeltsin", "age": 999, "country": "Russia"}
    assert presidents["Trump"] == {"name": "Trump", "age": 1337, "country": "US"}
    assert presidents["Big Man Tyrone"] == {
        "name": "Big Man Tyrone",
        "age": 101,
        "country": "Kekistan",
    }


def test_get_by_key_books_positive():
    """
    Passes if TableData class provides an access to table rows through dict[key] syntax
    """
    assert books["Farenheit 451"] == {"name": "Farenheit 451", "author": "Bradbury"}
    assert books["Brave New World"] == {"name": "Brave New World", "author": "Huxley"}
    assert books["1984"] == {"name": "1984", "author": "Orwell"}


def test_name_in_table_presidents():
    """
    Passes if containing check works correctly
    """
    assert "Yeltsin" in presidents
    assert "Trump" in presidents
    assert "Putin" not in presidents
    assert "Obama" not in presidents


def test_name_in_table_books():
    """
    Passes if containing check works correctly
    """
    assert "Farenheit 451" in books
    assert "1984" in books
    assert "The Witcher" not in books
    assert "The Lord of the Rings" not in books


def test_iter_presidents_positive():
    """
    Passes if iter implementation works correctly
    """
    lst = []
    for el in presidents:
        lst.append(el["name"])
    assert lst == ["Yeltsin", "Trump", "Big Man Tyrone"]


def test_iter_books_positive():
    """
    Passes if iter implementation works correctly
    """
    assert next(books) == {"name": "Farenheit 451", "author": "Bradbury"}
    assert next(books) == {"name": "Brave New World", "author": "Huxley"}
    assert next(books) == {"name": "1984", "author": "Orwell"}


def test_get_by_key_presidents_negative():
    """
    Passes if KeyError was raised to non existing key
    """
    with pytest.raises(KeyError):
        presidents["Putin"]


def test_get_by_key_books_negative():
    """
    Passes if KeyError was raised to non existing key
    """
    with pytest.raises(KeyError):
        books["The Witcher"]


def test_iter_presidents_negative():
    """
    Passes if StopIteration was raised at fourth call of next() ( 3 calls were before )
    """
    with pytest.raises(StopIteration):
        next(presidents)


def test_iter_books_negative():
    """
    Passes if StopIteration was raised at fourth call of next() ( 3 calls were before )
    """
    with pytest.raises(StopIteration):
        next(books)

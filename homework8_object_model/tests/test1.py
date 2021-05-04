# A test for homework8_object_model task1

from tempfile import NamedTemporaryFile

import pytest

from homework8_object_model.tasks.task1 import KeyValueStorage


@pytest.mark.parametrize(
    "data",
    [
        ("name=kek\nlast_name=top\npower=9001\nsong=shadilay"),
        ("name=ivan\nlast_name=ivanov\npower=2021\nsong=africa"),
    ],
)
def test_KeyValueStorage(data):
    """
    Passes if KeyValueStorage class guarantees access to data through attrs
    and dict methods ( var.key == dict[key] )
    Also if value can be treated as int it should be int
    """
    with NamedTemporaryFile(mode="w+", delete=False) as file:
        file.write(data)
        file.seek(0)
    first = KeyValueStorage(file.name)
    assert first.name == first["name"]
    assert first.last_name == first["last_name"]
    assert first.power == first["power"]
    assert first.song == first["song"]
    assert isinstance(first.power, int) is True


def test_negative_KeyValueStorage():
    """
    Passes if ValueError was raised to invalid key
    """
    data = "1=something"
    with NamedTemporaryFile(mode="w+", delete=False) as file:
        file.write(data)
        file.seek(0)
    with pytest.raises(ValueError):
        KeyValueStorage(file.name)


def test_another_negative():
    """
    Passes if AttributeError was raised to non existing instance attribute
    """
    data = "name=kek\nlast_name=top\npower=9001\nsong=shadilay"
    with NamedTemporaryFile(mode="w+", delete=False) as file:
        file.write(data)
        file.seek(0)
    with pytest.raises(AttributeError):
        second = KeyValueStorage(file.name)
        second.not_existing_attr

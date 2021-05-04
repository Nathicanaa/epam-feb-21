# A test to homework6_OOP2_Exceptions task1

from homework6_OOP2_Exceptions.tasks.task1 import instances_counter


@instances_counter
class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


def test_count_instance_before_init():
    """
    Passes if get_created_instances() is equal to 0 before initializing any instances
    """
    assert User.get_created_instances() == 0


def test_count_instance_after_init():
    """
    Passes if get_created_instances() is equal count of created instances
    and has the same behavior with an instance and a class
    """
    user_1, _, _ = (
        User("Ivan", "Ivanov"),
        User("Stepan", "Stepanov"),
        User("Vasiliy", "Vasiliev"),
    )
    assert user_1.get_created_instances() == 3
    assert User.get_created_instances() == 3


def test_init_attrs():
    """
    Passes if instances_counter decorator doesn't overwrite instances attributes
    """
    some_human = User("Alexander", "Alexandrov")
    assert (some_human.name, some_human.surname) == ("Alexander", "Alexandrov")


def test_reset_method():
    """
    Passes if reset_instances_counter() is equal to current
    state of counter and resets it after to 0
    """
    assert User.reset_instances_counter() == 4
    assert User.get_created_instances() == 0

# A test to homework6 task1

from homework6.tasks.task1 import instances_counter


@instances_counter
class User:
    pass


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
    user_1, _, _ = User(), User(), User()
    assert user_1.get_created_instances() == 3
    assert User.get_created_instances() == 3


def test_reset_method():
    """
    Passes if reset_instances_counter() is equal to current state of counter and resets it after to 0
    """
    assert User.reset_instances_counter() == 3
    assert User.get_created_instances() == 0

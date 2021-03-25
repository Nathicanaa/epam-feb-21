"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования

def instances_counter(cls):
    ""Some code""
    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
"""


def instances_counter(cls):
    """
    Takes a class and adds 2 new methods to it
    Args:
        cls: some class

    Returns: decorated class with 2 new methods get_created_instances and reset_instances_counter

    """
    setattr(cls, "counter_", 0)

    def __new__(cls, *args, **kwargs) -> cls:
        """
        Modified constructor which increases counter with every creation of new instance
        Args:
            cls: decorated class
            *args: pos args
            **kwargs: keyword args
        Returns: new object of a class
        """
        cls.counter_ += 1
        return super(cls, cls).__new__(cls)

    def get_created_instances(self=None) -> int:
        """
        Returns: current state of counter
        """
        return cls.counter_

    def reset_instances_counter(self=None) -> int:
        """
        Returns: last state of counter and resets it to 0
        """
        before_reset = cls.counter_
        cls.counter_ = 0
        return before_reset

    setattr(cls, "__new__", __new__)
    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)

    return cls

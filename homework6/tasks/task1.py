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
    setattr(cls, "counter", 0)

    def __init__(self, *args, **kwargs):
        """
        Modified constructor which increases counter with every init of new instance
        """
        cls.counter += 1
        self.args = args
        self.kwargs = kwargs

    def get_created_instances(self=None) -> int:
        """
        Returns: current state of counter
        """
        return cls.counter

    def reset_instances_counter(self=None) -> int:
        """
        Returns: last state of counter and resets it to 0
        """
        before_reset = cls.counter
        cls.counter = 0
        return before_reset

    setattr(cls, "__init__", __init__)
    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)

    return cls

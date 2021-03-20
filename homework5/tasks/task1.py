"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истело ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
"""
from datetime import datetime, timedelta
from typing import Optional


class Homework:
    """
    A class that describes homework( tasks ), has __init__ method and is_active
    """

    def __init__(self, text: str, deadline: int):
        """
        An instance construct
        Args:
            text: title of task
            deadline: days to finish task
        """
        self.text = text
        self.deadline = timedelta(deadline)
        self.created = datetime.today()

    def is_active(self) -> bool:
        """
        Checks if the deadline has been expired
        Returns: True if task is active, False otherwise
        """
        return self.deadline + self.created > datetime.today()


class Student:
    """
    A class that describes student, has __init__ and do_homework methods
    """

    def __init__(self, last_name: str, first_name: str):
        """
        An instance construct
        Args:
            last_name: str last name of a student
            first_name: str first name of a student
        """
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(hw_obj: Homework) -> Optional[Homework]:
        """
        Takes homework object and if it has not expired deadline returns incoming object
        otherwise returns None
        Args:
            hw_obj: an object of Homework class

        Returns: None if homework is not active anymore, otherwise returns
        incoming Homework object
        """
        if not hw_obj.is_active():
            print("You are late")
            return None
        return hw_obj


class Teacher:
    """
    A class that describes a teacher, has __init__ and create_homework methods
    """

    def __init__(self, last_name: str, first_name: str):
        """
        An instance construct
        Args:
            last_name: str last name of a teacher
            first_name: str first name of a teacher
        """
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """
        Takes title and deadline then returns Homework object
        Args:
            text: a title of new task
            deadline: days to finish new task
        Returns: new instance of Homework class

        """
        return Homework(text, deadline)

"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.

if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()


"""


from collections import defaultdict
from datetime import datetime, timedelta
from typing import Optional, TypeVar

HomeworkResult_obj = TypeVar("HomeworkResult_obj")


class DeadlineError(Exception):
    """
    Custom exception which will be raised if homework deadline is expired
    """

    pass


class Human:
    """
    Base class which makes only constructor
    """

    def __init__(self, last_name: str, first_name: str):
        """
        An instance construct
        Args:
            last_name: str last name of a Human
            first_name: str first name of a Human
        """
        self.last_name = last_name
        self.first_name = first_name


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


class Student(Human):
    """
    A class that describes student, has __init__ inherited from Human class
    and do_homework method
    """

    def do_homework(
        self, hw_obj: Homework, solution: str
    ) -> Optional[HomeworkResult_obj]:
        """
        Takes Homework object and Student's solution for this object
        Returns new HomeworkResult object if Homework object is not expired yet
        otherwise returns None
        Args:
            hw_obj: an object of Homework class
            solution: solution for given hw_obj

        Returns: None if homework is not active anymore, otherwise returns
        new HomeworkResult instance
        """
        if hw_obj.is_active():
            return HomeworkResult(author=self, homework=hw_obj, solution=solution)

        raise DeadlineError("You are late")


class HomeworkResult:
    """
    A class which describes a result of doing homework by a student
    has only __init__ method
    """

    def __init__(self, author: Student, homework: Homework, solution: str):
        """
        An instance construct
        raises TypeError of homework is not an instance of Homework class
        Args:
            author: a student doing homework
            homework: homework object to be done by a student
            solution: str result of doing homework by a student
        created: datetime object keeps time of creating object
        """
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.today()


class Teacher(Human):
    """
    A class that describes a teacher, has __init__ inherited from Human class
    has create_homework,check_homework and reset_results methods
    homework_done is a defaultdict with factory set to avoid duplicates, contains checked
    homeworks results
    """

    homework_done = defaultdict(set)

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

    def check_homework(self, homework_result: HomeworkResult) -> bool:
        """
        Checks student's result of doing homework, if len of student's solution is bigger than 5
        then the solution will be added to homework_done defaultdict
        Args:
            homework_result: HomeworkResult object to be checked by a teacher

        Returns: True if result successfully checked and added to homework_done
        otherwise False will be returned
        """
        if len(homework_result.solution) > 5:
            self.homework_done[homework_result.homework].add(homework_result.solution)
            return True

        return False

    @classmethod
    def reset_results(cls, homework: Homework = None) -> None:
        """
        Takes Homework object and removes it from homework_done defaultdict
        if Homework object is None then homework_done will be fully cleared
        Args:
            homework: a Homework object to be deleted from homework_done
        """
        if homework is None:
            cls.homework_done.clear()
        else:
            del cls.homework_done[homework]

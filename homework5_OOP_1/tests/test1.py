# A test for homework5_OOP_1 task1
from datetime import timedelta

from homework5_OOP_1.tasks.task1 import Homework, Student, Teacher

teacher = Teacher("Daniil", "Shadrin")
student = Student("Roman", "Petrov")
expired_homework = teacher.create_homework("Learn functions", 0)
oop_homework = teacher.create_homework("create 2 simple classes", 5)


def test_teacher_init():
    """Passes if init of teacher class works correctly"""
    assert teacher.last_name == "Daniil"
    assert teacher.first_name == "Shadrin"


def test_teacher_create_homework():
    """Passes if create_homework method of teacher class works correctly"""
    assert oop_homework.text == "create 2 simple classes"
    assert oop_homework.deadline == timedelta(5)


def test_student_init():
    """Passes if init of student class works correctly"""
    assert student.first_name == "Petrov"
    assert student.last_name == "Roman"


def test_student_do_homework_positive():
    """Passes if do_homework method of student class returns Homework instance"""
    assert type(student.do_homework(oop_homework)) == Homework


def test_student_do_homework_negative():
    """Passes if do_homework returns None"""
    assert student.do_homework(expired_homework) is None


def test_homework_init():
    """Passes of homework init works correctly"""
    assert expired_homework.text == "Learn functions"
    assert expired_homework.deadline == timedelta(0)


def test_homework_is_active():
    """Passes if is_active method returns bool types correctly"""
    assert expired_homework.is_active() is False
    assert oop_homework.is_active() is True

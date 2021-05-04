# A test for homework6_OOP2_Exceptions task 2
from datetime import timedelta

import pytest

from homework6_OOP2_Exceptions.tasks.task2 import (
    DeadlineError,
    Homework,
    HomeworkResult,
    Student,
    Teacher,
)

opp_teacher = Teacher("Daniil", "Shadrin")
advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

lazy_student = Student("Roman", "Petrov")
good_student = Student("Lev", "Sokolov")

oop_hw = opp_teacher.create_homework("Learn OOP", 1)
docs_hw = opp_teacher.create_homework("Read docs", 5)
expired_hw = advanced_python_teacher.create_homework("Make migrations", 0)

result_1 = good_student.do_homework(oop_hw, "I have done this hw")
result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
result_3 = lazy_student.do_homework(docs_hw, "done")


def test_teacher_names():
    """
    Passes if inherited init works correctly for Teacher class
    """
    assert (opp_teacher.last_name, opp_teacher.first_name) == ("Daniil", "Shadrin")
    assert (advanced_python_teacher.last_name, advanced_python_teacher.first_name) == (
        "Aleksandr",
        "Smetanin",
    )


def test_student_names():
    """
    Passes if inherited init works correctly for Student class
    """
    assert (lazy_student.last_name, lazy_student.first_name) == ("Roman", "Petrov")
    assert (good_student.last_name, good_student.first_name) == ("Lev", "Sokolov")


def test_teacher_create_homework_method():
    """
    Passes if Homework instances created correctly
    """
    assert (isinstance(oop_hw, Homework), isinstance(docs_hw, Homework)) == (True, True)
    assert (oop_hw.text, oop_hw.deadline) == ("Learn OOP", timedelta(1))
    assert (docs_hw.text, docs_hw.deadline) == ("Read docs", timedelta(5))


def test_homework_is_active():
    """
    Passes is_active() method checks correctly
    """
    assert oop_hw.is_active() is True
    assert docs_hw.is_active() is True
    assert expired_hw.is_active() is False


def test_homeworkresult_init():
    """
    Passes if Student's method do_homework() returns HomeworkResult instances
    """
    assert (
        isinstance(result_1, HomeworkResult),
        isinstance(result_2, HomeworkResult),
        isinstance(result_3, HomeworkResult),
    ) == (
        True,
        True,
        True,
    )


def test_homeworkresult_attrs():
    """
    Passes if HomeworkResult's instances created correctly
    """
    assert result_1.author.last_name == "Lev"
    assert result_1.homework.text == "Learn OOP"
    assert result_1.solution == "I have done this hw"


def test_homeworkresult_exeption():
    """
    Passes if TypeError was raised to non-Homework object
    """
    with pytest.raises(TypeError):
        HomeworkResult(good_student, "fff", "Solution")


def test_student_do_homework_exeption():
    """
    Passes if DeadlineError was raised to expired homework object
    """
    with pytest.raises(DeadlineError):
        good_student.do_homework(expired_hw, "this homework is expired")


def test_teacher_check_homework():
    """
    Passes if Teacher's method check_homework() works correctly
    """
    assert opp_teacher.check_homework(result_1) is True
    assert opp_teacher.check_homework(result_2) is True
    assert opp_teacher.check_homework(result_3) is False


def test_teacher_homework_done_access():
    """
    Passes if an access to homework_done through the class itself and an instances are the same
    """
    assert Teacher.homework_done is opp_teacher.homework_done


def test_teacher_homework_done_duplicates():
    """
    Passes if homework_done doesn't contain duplicated solutions for homeworks
    """
    new_homework = opp_teacher.create_homework("Learn Falcon + PyPy", 2)
    res = good_student.do_homework(new_homework, "I have it already learned")
    advanced_python_teacher.check_homework(res)

    result_4 = lazy_student.do_homework(oop_hw, "I have done this hw")
    result_5 = lazy_student.do_homework(docs_hw, "I have done this hw too")

    advanced_python_teacher.check_homework(result_1)
    advanced_python_teacher.check_homework(result_2)
    advanced_python_teacher.check_homework(result_4)
    advanced_python_teacher.check_homework(result_5)

    opp_teacher.check_homework(result_1)
    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_4)
    opp_teacher.check_homework(result_5)

    assert len(Teacher.homework_done) == 3


def test_teacher_reset_results():
    """
    Passes if reset_results() method with given Homework object removes exactly this
    object from homework_done and clears totally if Homework object wasn't given
    """
    Teacher.reset_results(oop_hw)
    assert len(Teacher.homework_done) == 2
    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0

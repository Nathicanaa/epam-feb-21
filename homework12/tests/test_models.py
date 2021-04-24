# A test for homework12 models
# For all Homework instances 'created' attr was created manually because it
# wont be generated automatically until instances aren't committed to a Session

import pprint
import sys
from datetime import datetime

pprint.pprint(sys.path)

from homework12.models import Homework, HomeworkResult, Student, Teacher

opp_teacher = Teacher(name="Daniil", last_name="Shadrin")
advanced_python_teacher = Teacher(name="Aleksandr", last_name="Smetanin")

lazy_student = Student(name="Roman", last_name="Petrov")
good_student = Student(name="Lev", last_name="Sokolov")


oop_hw = Homework(
    text="Learn OOP", deadline=1, teacher=opp_teacher, created=datetime.today()
)
docs_hw = Homework(
    text="Read docs", deadline=5, teacher=opp_teacher, created=datetime.today()
)
expired_hw = Homework(
    text="Make migrations",
    deadline=0,
    teacher=advanced_python_teacher,
    created=datetime.today(),
)

result_1 = HomeworkResult(
    student=good_student, homework=oop_hw, solution="I have done this hw"
)
result_2 = HomeworkResult(
    student=good_student, homework=docs_hw, solution="I have done this hw too"
)
result_3 = HomeworkResult(student=lazy_student, homework=docs_hw, solution="done")
result_4 = HomeworkResult(
    student=lazy_student, homework=expired_hw, solution="deadline is over:("
)


def test_names():
    """
    Passes if names and last names represented correct
    """
    assert repr(opp_teacher) == "Daniil Shadrin"
    assert opp_teacher.name, opp_teacher.last_name == ("Daniil", "Shadrin")
    assert repr(advanced_python_teacher) == "Aleksandr Smetanin"
    assert repr(lazy_student) == "Roman Petrov"
    assert repr(good_student) == "Lev Sokolov"
    assert good_student.name, good_student.last_name == ("Lev", "Sokolov")


def test_homeworks_statuses():
    assert oop_hw.is_active is True
    assert docs_hw.is_active is True
    assert expired_hw.is_active is False


def test_bounds_homework_teacher():
    assert oop_hw.teacher == opp_teacher
    assert oop_hw.teacher_id == opp_teacher.id
    assert docs_hw.teacher == opp_teacher
    assert oop_hw, docs_hw in opp_teacher.homeworks_created
    assert expired_hw in advanced_python_teacher.homeworks_created


def test_homeworks_result_():
    assert repr(result_1.student) == "Lev Sokolov"
    assert result_1.student_id == good_student.id
    assert result_1.homework == oop_hw
    assert result_1.homework_id == oop_hw.id
    assert result_1.homework.text == "Learn OOP"
    assert result_1 in oop_hw.homework_results

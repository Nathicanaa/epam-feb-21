"""
A test for get_report.py
1) save the current count of not expired homeworks
2) Add to table 5 expired homeworks
3) Call write_to_csv()
4) Assert count of not expired homeworks haven't changed
"""
from homework12.get_report import write_to_csv
from homework12.models import Homework, HomeworkResult, Student, Teacher
from homework12.session_scope import session_scope


def count_csv_rows():
    with open("get_report.csv", "r", encoding="utf-8") as file:
        return len(file.readlines())


LEN_1 = count_csv_rows()

with session_scope() as session:
    some_teacher = Teacher(name="Ivan", last_name="Ivanov")

    some_student = Student(name="Nikolay", last_name="Nikolaev")

    exp_hw_1 = Homework(
        text="first expired homework", deadline=-10, teacher=some_teacher
    )
    exp_hw_2 = Homework(
        text="another expired homework", deadline=-1, teacher=some_teacher
    )
    exp_hw_3 = Homework(text="one more!", deadline=-100, teacher=some_teacher)
    exp_hw_4 = Homework(text="and another one!", deadline=0, teacher=some_teacher)
    exp_hw_5 = Homework(
        text="aah .... he we go again", deadline=-777, teacher=some_teacher
    )

    hw_res_expired_1 = HomeworkResult(
        solution="one", student=some_student, homework=exp_hw_1
    )
    hw_res_expired_2 = HomeworkResult(
        solution="two", student=some_student, homework=exp_hw_2
    )
    hw_res_expired_3 = HomeworkResult(
        solution="three", student=some_student, homework=exp_hw_3
    )
    hw_res_expired_4 = HomeworkResult(
        solution="four", student=some_student, homework=exp_hw_4
    )
    hw_res_expired_5 = HomeworkResult(
        solution="five", student=some_student, homework=exp_hw_5
    )

    session.add_all(
        [
            hw_res_expired_1,
            hw_res_expired_2,
            hw_res_expired_3,
            hw_res_expired_4,
            hw_res_expired_5,
        ]
    )

write_to_csv()

LEN_2 = count_csv_rows()


def test_changes_in_csv():
    """
    Passes if count of not expired homeworks haven't changed after
    adding 5 expired homeworks
    """
    assert LEN_2 == LEN_1

"""'manual_migration'

Revision ID: a9717d807aad
Revises: c4bb4a2c1279
Create Date: 2021-04-24 18:42:55.415717

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
from homework12_alembic_sqlalchemy.models import (
    Homework,
    HomeworkResult,
    Student,
    Teacher,
)
from homework12_alembic_sqlalchemy.session_scope import session_scope

revision = "a9717d807aad"
down_revision = "c4bb4a2c1279"
branch_labels = None
depends_on = None


def upgrade():
    """
    This migration script is written manually
    """
    with session_scope() as session:
        opp_teacher = Teacher(name="Daniil", last_name="Shadrin")
        advanced_python_teacher = Teacher(name="Aleksandr", last_name="Smetanin")

        lazy_student = Student(name="Roman", last_name="Petrov")
        good_student = Student(name="Lev", last_name="Sokolov")

        oop_hw = Homework(text="Learn OOP", deadline=1, teacher=opp_teacher)
        docs_hw = Homework(text="Read docs", deadline=5, teacher=opp_teacher)
        expired_hw = Homework(
            text="Make migrations", deadline=0, teacher=advanced_python_teacher
        )

        result_1 = HomeworkResult(
            student=good_student, homework=oop_hw, solution="I have done this hw"
        )
        result_2 = HomeworkResult(
            student=good_student, homework=docs_hw, solution="I have done this hw too"
        )
        result_3 = HomeworkResult(
            student=lazy_student, homework=docs_hw, solution="done"
        )
        result_4 = HomeworkResult(
            student=lazy_student, homework=expired_hw, solution="deadline is over:("
        )
        session.add_all([result_1, result_2, result_3, result_4])


def downgrade():
    """
    This migration script is written manually
    """
    with session_scope() as session:
        session.query(Student).delete()
        session.query(Teacher).delete()
        session.query(Homework).delete()
        session.query(HomeworkResult).delete()

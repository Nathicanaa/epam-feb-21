"""'creating_tables'

Revision ID: c4bb4a2c1279
Revises:
Create Date: 2021-04-24 18:42:54.811169

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c4bb4a2c1279"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "students",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("last_name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "teachers",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("last_name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "homeworks",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("text", sa.String(length=255), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("deadline", sa.Integer(), nullable=False),
        sa.Column("teacher_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["teacher_id"],
            ["teachers.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "Homework_results",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("solution", sa.String(length=255), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("student_id", sa.Integer(), nullable=True),
        sa.Column("homework_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["homework_id"],
            ["homeworks.id"],
        ),
        sa.ForeignKeyConstraint(
            ["student_id"],
            ["students.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("Homework_results")
    op.drop_table("homeworks")
    op.drop_table("teachers")
    op.drop_table("students")
    # ### end Alembic commands ###

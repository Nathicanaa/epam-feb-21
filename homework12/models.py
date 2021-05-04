from datetime import datetime, timedelta

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Human(Base):
    """
    Abstract Human class for Teacher and Student
    Has id, name and last name columns
    Also has __repr__ dunder for printing name and last
    name if print was called to Student's or Teacher's instances
    """

    __abstract__ = True

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    def __repr__(self) -> str:
        return f"{self.name} {self.last_name}"


class Student(Human):
    """
    Student class inherited from Human, has same columns and repr method
        homeworks_done : a bind to HomeworkResult attribute 'student' which shows who
    made particular homework done
    """

    __tablename__ = "students"

    homeworks_done = relationship("HomeworkResult", back_populates="student")


class Teacher(Human):
    """
    Teacher class inherited from Human, has same columns and repr method
        homeworks_created : a bind to HomeworkResult attribute 'teacher' which shows who
    created particular homework
    """

    __tablename__ = "teachers"

    homeworks_created = relationship("Homework", back_populates="teacher")


class Homework(Base):
    """
    Homework class which represents table for all homeworks,
    has dunder repr method
    columns:
        id: primary key
        text: a text description of the homework
        created: date and time of homework object creating
        deadline: days to complete particular homework
        teacher_id: id of the teacher who created this homework
    binds:
        teacher: a bind to Teacher's class 'homeworks_created' attribute
        homework_results: a bind to HomeworkResult's class 'homework' attribute
        which represents the solution of particular homework
    properties:
        is_active: returns True if homework isn't expired, False otherwise
    methods:
        __repr__: prints Homework instance's attributes if print was
        called to this instance
    """

    __tablename__ = "homeworks"

    id = Column(Integer, autoincrement=True, primary_key=True)
    text = Column(String(255), nullable=False)
    created = Column(DateTime, default=datetime.today(), nullable=False)
    deadline = Column(Integer, nullable=False)

    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship(Teacher, back_populates="homeworks_created")

    homework_results = relationship("HomeworkResult", back_populates="homework")

    @property
    def is_active(self) -> bool:
        """
        Checks homework for being expired
        Returns: True if homework is active, False otherwise
        """
        return self.created + timedelta(self.deadline) > datetime.today()

    def __repr__(self) -> str:
        return (
            f"text - {self.text}\n"
            f"deadline - {self.deadline}\n"
            f"is_active - {self.is_active}\n"
            f"created - {self.created}\n"
            f"teacher - {self.teacher}\n"
            f"res - {self.homework_results}\n"
        )


class HomeworkResult(Base):
    """
    HomeworkResult class which represents table for all solutions of homeworks,
    has dunder repr method
    columns:
        id: primary key
        solution: a solution for some homework
        created: date and time of solution object creating
        student_id: id of the student who made this solution
        homework_id: id of the homework which was solved with
        this solution object
    binds:
        student: a bind to Student's class 'homeworks_done' attribute
        homework: a bind to Homework's class 'homework_results' attribute
    methods:
        __repr__: prints HomeworkResult instance's attributes if print was
        called to this instance
    """

    __tablename__ = "Homework_results"

    id = Column(Integer, autoincrement=True, primary_key=True)
    solution = Column(String(255), nullable=False)
    created = Column(DateTime, default=datetime.today(), nullable=False)

    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship(Student, back_populates="homeworks_done")

    homework_id = Column(Integer, ForeignKey("homeworks.id"))
    homework = relationship(Homework, back_populates="homework_results")

    def __repr__(self) -> str:
        return (
            f"homework - {self.homework.text}\n"
            f"solution - {self.solution}\n"
            f"created - {self.created}\n"
            f"student - {self.student}\n"
        )

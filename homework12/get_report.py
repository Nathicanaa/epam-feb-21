import csv
from datetime import datetime, timedelta

from models import HomeworkResult
from session_scope import session_scope


def get_data() -> "sqlalchemy.query":
    """
    Gets all HomeworkResult instances from the table "Homework_results" and returns it as a query
    Returns: a query with all rows in "Homework_results" table
    """
    with session_scope() as session:
        return session.query(HomeworkResult)


def write_to_csv() -> None:
    """
    Takes a query with all rows in the table "Homework_results", filters expired homeworks
    and writes it to a csv file 'get_report.csv'
    """
    with open("tests/get_report.csv", "w", encoding="utf-8") as file:
        file_writer = csv.writer(file, lineterminator="\r")
        file_writer.writerow(
            ["Student", "Homework creating date", "Teacher", "Homework text"]
        )
        for row in get_data():
            if (
                row.homework.created + timedelta(row.homework.deadline)
                > datetime.today()
            ):
                file_writer.writerow(
                    [
                        row.student,
                        row.homework.created,
                        row.homework.teacher,
                        row.homework.text,
                    ]
                )


if __name__ == "__main__":
    write_to_csv()

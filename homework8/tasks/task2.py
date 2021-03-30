"""
Write a wrapper class TableData for database table, that when initialized
with database name and table acts as collection object (implements Collection protocol).
Assume all data has unique values in 'name' column.
So, if
__
presidents = TableData(database_name='example.sqlite', table_name='presidents')

then len(presidents) will give current amount of rows in presidents table in database

presidents['Yeltsin'] should return single data row for president with name Yeltsin

'Yeltsin' in presidents should return if president with same name exists in table

object implements iteration protocol. i.e. you could use it in for loops::
for president in presidents:
    print(president['name'])
__
all above mentioned calls should reflect most recent data.
If data in table changed after you created collection instance, your calls should return updated data.

Avoid reading entire table into memory. When iterating through records, start reading the first record,
then go to the next one, until records are exhausted. When writing tests,
it's not always necessary to mock database calls completely.
Use supplied example.sqlite file as database fixture file.
"""
import sqlite3
from typing import Iterator, Optional, Tuple


class TableData:
    """
    A class to work with sqlite3 database through containing methods.
    Contains methods:
        __connect
        __take_column_names
        __init__
        __len__
        __getitem__
        __contains
        __iter__
        __next__
    """

    def __connect(self, sql_query: str) -> sqlite3.Cursor:
        """
        A method which takes sql query and returns executed cursor
        Args:
            sql_query: some sql query
        Returns: execute of sql query
        """
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            return cur.execute(sql_query)

    def __take_column_names(self) -> Tuple:
        """
        Reads table and returns names of table columns
        Returns: tuple of column names of given table
        """
        cur = self.__connect(f"SELECT * FROM {self.table_name} LIMIT 1")
        columns = tuple(map(lambda x: x[0], cur.description))
        return columns

    def __init__(self, db_name: str, table_name: str):
        """
        Constructor method, takes database name and table name into this database
        Args:
            db_name: name of database
            table_name: name of table into database
        Init:
            self.columns: tuple of column names in table
            self.row: all rows of given table
        """
        self.db_name = db_name
        self.table_name = table_name
        self.columns = self.__take_column_names()
        self.rows = self.__connect(f"SELECT * FROM {self.table_name}")

    def __len__(self) -> int:
        """
        A method to count of rows into table
        Returns: count of rows
        """
        cur = self.__connect(f"SELECT COUNT(*) FROM {self.table_name}")
        return cur.fetchone()[0]

    def __getitem__(self, name: str) -> Optional[dict]:
        """
        Method to get access to table data through dict concept dict[key]
        Returns whole row containing name=name
        Raises KeyError if name not in table
        Args:
            name: some name to be a key for row getting
        Returns: row where name=name
        """
        cur = self.__connect(f"SELECT * FROM {self.table_name} WHERE name='{name}'")
        if row := cur.fetchone():
            return dict(zip(self.columns, row))
        raise KeyError(f"Name {name} doesn't exist in {self.table_name} table!")

    def __contains__(self, name: str) -> bool:
        """
        Checks name for being into table
        Args:
            name: some name
        Returns: True if name in table False otherwise
        """
        cur = self.__connect(f"SELECT * FROM {self.table_name}")
        return name in (el[0] for el in cur.fetchall())

    def __iter__(self) -> Iterator:
        """
        Magic method to implement iteration protocol
            Returns: object itself
        """
        return self

    def __next__(self) -> Optional[dict]:
        """
        Another magic method to implement iteration protocol
        Returns: next row of object
        """
        if row := self.rows.fetchone():
            return dict(zip(self.columns, row))
        raise StopIteration

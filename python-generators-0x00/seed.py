#!/usr/bin/python3
import mysql.connector
from mysql.connector import MySQLConnection
from typing import TypedDict


class User(TypedDict):
    """ This is a custom type for user that exists in database.
    """
    name: str
    email: str
    age: int


def connect_db(dbname: str = '', attempts: int = 3) -> MySQLConnection:
    """This function tries to connect to database maximum 3 times
    if the connection established successfully the function
    will return an object to the established connection otherwise
    it will return None.

    Args:
        attempts (int, optional): This is the number of attempts for the user
        to connect to the mysql server. Defaults to 3.

    Returns:
        MySQLConnection: This is a connection to the mysql server.
    """
    while attempts > 0:
        try:
            attempts -= 1
            connection = mysql.connector.connect(
                host="127.0.0.1",
                port=3306,
                user="root",
                password="Za158269347",
                dbname=dbname
            )
            return connection
        except Exception as e:
            print(f"Attempts remaining: {attempts}")
            print("Error: ", e)
    return None


def create_database(connection: MySQLConnection) -> None:
    """
    This function creates a database in the given mysql server

    Args:
        connection (Connection): This is an object to the mysql server
        connection
    """

    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
    except Exception as err:
        print("Error creating database", err)


def connect_to_prodev() -> None:
    """ This function connects the mysql server to the database
        ALX_prodev
    """

    return connect_db("ALX_prodev")


def create_table(connection: MySQLConnection) -> None:
    """ This function creates a table in the database ALX_prodev if the
        table doesn't exist.

    Args:
        connection (MySQLConnection): This is an object to the connection
        that connects to the mysql server.
    """

    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                INDEX idx_user_id (user_id)
            )
        """)
        connection.commit()
        cursor.close()
    except Exception as err:
        print("Error creating database", err)


def insert_data(connection: MySQLConnection, filePath: str) -> None:
    """ This function inserts the data from the given file into the
        database specified in the given connection.

    Args:
        connection (MySQLConnection): This is the connection to the database
        to insert the data into its tables.

        data (Dict): This is a dictionary of the data to be inserted into
        database
    """

    try:
        cursor = connection.cursor()
        reader_generator = readFileLineByLine("user_data.csv")
        next(reader_generator)
        for row in reader_generator:
            cursor.execute(
                """ INSERT INTO user_data
                        (user_id, name, email, age)
                        VALUES (UUID(), %s, %s, %s)
                """,
                [row[0], row[1], row[2]]
            )
        connection.commit()
        cursor.close()
    except Exception as err:
        print("Failed to insert into database", err)


def readFileLineByLine(filePath):
    """This is a generator function that reads file line by line

    Args:
        filePath (str): The path to the file to read.

    Returns:
        Generator: a generator which produces the next line in the
        file being read
    """
    with open(filePath, "r") as fd:
        return (list(map(lambda x: x[1:-1], line.rstrip().split(","))) for line in fd.readlines())

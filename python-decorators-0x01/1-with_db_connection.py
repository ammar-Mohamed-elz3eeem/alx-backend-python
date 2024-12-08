import sqlite3
import functools


def with_db_connection(func):
    """ This function creates a context manager when making connections
        to database.

    Args:
        func: This is the function that requires a connection to database.
    """
    def with_db_connection_wrapper(*args, **kwargs):
        with sqlite3.connect("users.db") as conn:
            result = func(conn, *args, **kwargs)
            return result
    return with_db_connection_wrapper


@with_db_connection
def get_user_by_id(conn, user_id):
    """ This function gets a single user from database using
        user id

    Args:
        conn (MySQLConnection): This is the connection needed to
        connect to database.

        user_id (int): This is the user id to get from database.

    Returns:
        RowType: The user with the given id retrieved from database.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


# Fetch user by ID with automatic connection handling
user = get_user_by_id(user_id=1)
print(user)

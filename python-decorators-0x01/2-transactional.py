import sqlite3
import functools


def with_db_connection(func):
    """ This function creates a context manager when making connections
        to database.

    Args:
        func: This is the function that requires a connection to database.
    """
    functools.wraps(func)

    def with_db_connection_wrapper(*args, **kwargs):
        with sqlite3.connect("users.db") as conn:
            result = func(conn, *args, **kwargs)
            return result
    return with_db_connection_wrapper


def transactional(func):
    """ This function adds a transaction layer over database
        query excutions.

    Args:
        func: This is the function to add transaction layer to.

    Returns:
        func after applying the transaction into it.
    """
    functools.wraps(func)

    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            print("Transaction Failed", e)
            raise
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    """ This function updates user email with the given
        new_email based on the given user_id.

    Args:
        conn (MySQLConnection): This is the connection of the database.

        user_id (int): This is the id of the user to update its email.

        new_email (str): This is the new email for the user.
    """
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?",
                   (new_email, user_id))


# Update user's email with automatic transaction handling
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')

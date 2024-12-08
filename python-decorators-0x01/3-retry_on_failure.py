import time
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


def retry_on_failure(retries=3, delay=1):
    """ This function retries the function of a certain number of times if it
        raises an exception

    Args:
        retries (int, optional): number of times to retry to call
        the function. Defaults to 3.

        delay (int, optional): the delay between every call the function in
        case it failed on the first try. Defaults to 1.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exception = None
            while retries > 0:
                retries -= 1
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    last_exception = err
                    print(
                        f"Failed, Attempts remaining: {retries}, Retrying in {delay} seconds...")
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# attempt to fetch users with automatic retry on failure


users = fetch_users_with_retry()
print(users)

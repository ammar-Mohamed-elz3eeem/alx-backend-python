import time
import sqlite3
import functools


query_cache = {}

"""your code goes here"""


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


def cache_query(func):
    """This function caches query results based on the SQL query string

    Args:
        func: This is the function to add query caching to it
    """
    def wrapper(*args, **kwargs):
        query = kwargs.get("query", args[1] if len(args) > 1 else None)
        if query in query_cache:
            print("This query result is from cached version")
            return query_cache[query]

        result = func(*args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")

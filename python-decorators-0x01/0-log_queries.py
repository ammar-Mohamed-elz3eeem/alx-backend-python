import sqlite3
import functools

# decorator to lof SQL queries

""" YOUR CODE GOES HERE"""


def log_queries(func):
    """ This is a wrapper function for log_queries function
        it will handle printint out queries passed to database.

    Args:
        func (Function): This is the function to wrap

    Returns:
        wrapper: This is the wrapper function that will wrap log_queries
        function.
    """
    @functools.wraps(func)
    def log_queries_wrapper(*args, **kwargs):
        query = kwargs.get("query", query if len(args)
                           > 0 and args[0] else None)
        if query:
            print(f"[Database::Query::Excution]: {query}")
        return func(*args, **kwargs)
    return log_queries_wrapper


@log_queries
def fetch_all_users(query):
    """This function gets all users from database.

    Args:
        query (str): This is the query to excute.

    Returns:
        RowType: This is the result of the query excuted.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# fetch users while logging the query
users = fetch_all_users(
    query="CREATE TABLE users(id int PRIMARY KEY, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL);")

#!/usr/bin/python3
import seed
from typing import Generator, Tuple


def stream_users() -> Generator[Tuple[seed.User, ...], None, None]:
    """ This function uses a generator to fetch rows one by one
        from the user_data table.

    Raises:
        ValueError: if the connection is not established correctly
        or there is an error on connecting to database.

    Yields:
        RowType: Single result from the database.
    """

    try:
        connection = seed.connect_to_prodev()
        if connection is None:
            raise ValueError("Connection is not established")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data;")
        for row in cursor:
            yield row
    except Exception as err:
        print("can't read data from database", err)

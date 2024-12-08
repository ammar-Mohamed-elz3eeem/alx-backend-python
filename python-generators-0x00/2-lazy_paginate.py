from seed import connect_to_prodev, User
from typing import Generator, Tuple


def lazy_paginate(page_size: int) -> Generator[Tuple[str, ...], None, None]:
    """ This function gets data from database in chunks to be
        put in pages.

    Args:
        page_size (int): This is the maximum number of users per page.

    Yields:
        Generator: The users from database in chunks.
    """
    offset = 0
    connection = connect_to_prodev()
    cursor = connection.cursor()
    while True:
        try:
            cursor.execute(
                "SELECT * FROM user_data LIMIT %s OFFSET %s", [page_size, offset])

            result = cursor.fetchall()
            if not result:
                break

            yield result
            offset += page_size
        except Exception as err:
            print("Failed to read from database", err)

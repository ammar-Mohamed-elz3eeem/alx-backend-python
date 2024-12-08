import seed
from typing import Generator, Tuple, List


def paginate_users(page_size: int, offset: int) -> List[Tuple[str, ...]]:
    """ This function returns number of users from database equal to
        page_size at the given offset

    Args:
        page_size (int): This is maximum number of users to return
        offset (int): This is the offset to get start count users from

    Returns:
        List[Tuple[str, ...]]: List of all users
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_paginate(page_size: int) -> Generator[Tuple[str, ...], None, None]:
    """ This function gets data from database in chunks to be
        put in pages.

    Args:
        page_size (int): This is the maximum number of users per page.

    Yields:
        Generator: The users from database in chunks.
    """
    offset = 0
    while True:
        try:
            result = paginate_users(page_size, offset)

            if not result:
                break

            yield result

            offset += page_size
        except Exception as err:
            print("Failed to read from database", err)

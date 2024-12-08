from seed import connect_to_prodev, User
from typing import Generator, List


def stream_users_in_batches(batch_size: int) -> Generator[List[User], None, None]:
    """ This function fetches rows from database in batches.

    Args:
        batch_size (int): This is the required batch size.

    Yields:
        Generator[List[User], None, None]: The rows from database.
    """

    try:
        connection = connect_to_prodev()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data")

        users = [{"id": row[0], "name": row[1], "email": row[2],
                  "age": row[3]} for row in cursor.fetchall()]

        for i in range(0, len(users), batch_size):
            yield users[i:i + batch_size]
        return True
    except Exception as err:
        print("Failed to read from database", err)
        return False


def batch_processing(batch_size: int) -> Generator[User, None, None]:
    """ This function process each batch of the users coming from
        database to filter them and yields only users with age over 25.

    Args:
        batch_size (int): This is the single batch size.

    Yields:
        Generator[List[User], None, None]: only users with age over 25.
    """

    print("HERE")
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                yield user
    return True

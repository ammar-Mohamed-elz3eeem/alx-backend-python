from seed import connect_to_prodev
from typing import Generator, Tuple


def stream_user_ages() -> Generator[Tuple[int, ...], None, None]:
    """ This function streams ages from database table and
        yield them one by one.

    Yields:
        Generator[Tuple[int, ...], None, None]: ages of users one by one.
    """

    try:
        connection = connect_to_prodev()
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")
        for age in cursor:
            # print(age)
            yield age[0]
        connection.close()
    except:
        print("can't read from database")


def calculate_average_ages():
    """ This function calculates the average of all ages that
        exist in database table using generator streaming.

    Returns:
        int: average of all ages.
    """

    user_ages = stream_user_ages()
    length = 0
    total = 0
    for age in user_ages:
        total += age
        length += 1
    return total / length

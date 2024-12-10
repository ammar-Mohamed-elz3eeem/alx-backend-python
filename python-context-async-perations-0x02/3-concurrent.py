import asyncio
import aiosqlite


async def async_fetch_users():
    """ This function returns all users from the database
        asyncronously.

        Returns:
            List of all users in the database.
    """

    async with aiosqlite.connect("users.db") as conn:
        return await conn.execute_fetchall("SELECT * FROM users")


async def async_fetch_older_users():
    """ This function returns all users from the database
        where user's age is greater than 40 asyncronously.

        Returns:
            List of all users that are greater than 40 years
            in the database.
    """

    async with aiosqlite.connect("users.db") as conn:
        return await conn.execute_fetchall("SELECT * FROM users WHERE age > 40")


async def fetch_concurrently():
    return await asyncio.gather(async_fetch_users(), async_fetch_older_users())


print(asyncio.run(fetch_concurrently()))

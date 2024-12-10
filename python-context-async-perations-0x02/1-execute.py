from mysql import connector
from typing import Any, List
from mysql.connector import MySQLConnection

class ExecuteQuery():
    def __init__(self, query: str, params: List[Any]) -> None:
        """ This is the default constructor for ExecuteQuery object
            and is used to connect to the database and initialize the
            cursor object to be used to excute quiries in database.

        Args:
            config (str)
                This is the mysql server configurations
        """
        config = {
            "database": "ALX_prodev",
            "user": "root",
            "host": "localhost",
            "password": "Za158269347",
        }
        self.connection = connector.connect(**config)
        self.cursor = self.connection.cursor()
        self.cursor.execute(query, params)

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        """ This method is called to release the db connection
            and it also handles if any exception happens

        Args:
            exc_type (Exception)
                This is the type of exception.
            
            exc_value (str)
                This is the message of the exception.
            
            exc_tb (_type_)
                This is the exception traceback.
        """
        self.cursor.close()
        self.connection.close()

    def __enter__(self) -> Any:
        """ This method is used when to return the connection cursor.

        Returns:
            CMySQLCursor
                This is the cursor that is used to do operations
               on database.
        """
        return self.cursor.fetchall()

with ExecuteQuery("SELECT * FROM users WHERE age > %s", [25]) as data:
    print(data)

from mysql import connector
from typing import Dict, Tuple, List
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor

class DatabaseConnection():
    def __init__(self, config: Dict[str, str]) -> None:
        """ This is the default constructor for DatabaseConnection object
            and is used to connect to the database and initialize the
            cursor object to be used to excute quiries in database.

        Args:
            config (Dict[str, str])
                This is the mysql server configurations
        """
        self.connection = connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __exit__(self, exc_type: Exception, exc_value: str, exc_tb) -> None:
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

    def __enter__(self) -> MySQLCursor:
        """ This method is used when to return the connection cursor.

        Returns:
            CMySQLCursor
                This is the cursor that is used to do operations
               on database.
        """
        return self.cursor

config = {
    "database": "ALX_prodev",
    "user": "root",
    "host": "localhost",
    "password": "Za158269347",
}

with DatabaseConnection(config) as conn:
    conn.execute("SELECT * FROM users")
    data = conn.fetchall()
    print(data)

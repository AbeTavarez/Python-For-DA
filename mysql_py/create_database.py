# ===================================== #
# CREATE DATABASE EXAMPLE USING PYTHON  #
# ===================================== #

import mysql.connector
from mysql.connector import Error

connection = None
cursor = None

try:
    # Connect to the server ONLY (not a specific DB)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        
        # The SQL command to create the database
        db_name = "registration_db"
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        
        print(f"Database '{db_name}' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if connection is not None and connection.is_connected():
        if cursor is not None:
            cursor.close()
        connection.close()
        print("MySQL connection is closed")
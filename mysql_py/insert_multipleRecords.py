import mysql.connector as mydbconnection
from mysql.connector import Error

conn = None
cursor = None

try:
    # Create a new connection
    conn = mydbconnection.connect(database='usersdb', user='root',password='root', port ='3306')

    # Create SQL Query
    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES (%s, %s, %s, %s) """

    # List of records (in a list of tuples)
    records_to_insert = [(4, 'HP Pavilion Power', 1999, '2019-01-11'),
                         (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
                         (6, 'Microsoft Surface', 2330, '2019-07-23')]
    # Create Cursor
    cursor = conn.cursor()
    
    # Execute Many: uses the query and the list of records to execute multiple inserts
    cursor.executemany(mySql_insert_query, records_to_insert)
    
    # Commit saves the changes
    conn.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")

except Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if conn is not None and conn.is_connected():
        if cursor is not None:
            cursor.close()
        conn.close()
        print("MySQL connection is closed")

from utils_q1.dbconnection_q1 import getDBConnection

# To execute CREATE, UPDATE and DELETE query

def executeQuery(query):
    connection = getDBConnection()

    cursor = connection.cursor()

    cursor.execute(query)

    connection.commit()

    cursor.close()

    connection.close()

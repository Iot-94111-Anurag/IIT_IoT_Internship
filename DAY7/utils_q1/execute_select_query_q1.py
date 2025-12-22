from utils_q1.dbconnection_q1 import getDBConnection

# To execute retrive Query

def executeSelectQuery(query):
    connection = getDBConnection()

    cursor = connection.cursor()

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()

    connection.close()
    
    return data

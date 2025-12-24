from dbconnection import getconnection

def executeQuery(query):
    conn = getconnection()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

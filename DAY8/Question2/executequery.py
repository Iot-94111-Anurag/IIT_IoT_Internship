from dbconnection import getconnection

def executeQuery(query):
    con = getconnection()
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()

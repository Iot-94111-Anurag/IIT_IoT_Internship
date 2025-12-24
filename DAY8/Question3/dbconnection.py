import mysql.connector

def getconnection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="health_monitoring_system"
    )

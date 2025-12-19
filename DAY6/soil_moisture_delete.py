import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="smart_agriculture"
)

# User input
sensor_id = int(input("Enter sensor ID to delete: "))

# DELETE query
cursor = connection.cursor()
cursor.execute(
    "DELETE FROM soil_moisture WHERE sensor_id=%s",
    (sensor_id,)
)
connection.commit()

cursor.close()
connection.close()

print(f"Record with sensor ID {sensor_id} deleted successfully!")

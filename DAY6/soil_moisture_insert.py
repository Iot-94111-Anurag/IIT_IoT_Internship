import mysql.connector
from datetime import datetime

# Connect to MySQL
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="smart_agriculture"
)

# User input
sensor_id = int(input("Enter sensor ID: "))
moisture_level = float(input("Enter moisture level: "))

# Use current timestamp
reading_time = datetime.now()

# Insert query
query = "INSERT INTO soil_moisture (sensor_id, moisture_level, reading_time) VALUES (%s, %s, %s)"
data = (sensor_id, moisture_level, reading_time)

cursor = connection.cursor()
cursor.execute(query, data)
connection.commit()

cursor.close()
connection.close()

print("Data inserted successfully!")

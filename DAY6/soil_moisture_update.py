import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="smart_agriculture"
)

# User input
sensor_id = int(input("Enter sensor ID: "))
moisture_level = float(input("Enter new moisture level: "))

# Simple UPDATE query
cursor = connection.cursor()
cursor.execute(
    "UPDATE soil_moisture SET moisture_level=%s WHERE sensor_id=%s",
    (moisture_level, sensor_id)
)
connection.commit()

cursor.close()
connection.close()

print("Data updated successfully!")

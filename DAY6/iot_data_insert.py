import mysql.connector
from datetime import datetime

# Connect to MySQL
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data",
    use_pure=True
)

# User input
id = int(input("Enter id: "))
temperature = float(input("Enter temperature: "))
humidity = float(input("Enter humidity: "))
timestamp_str = input("Enter timestamp (YYYY-MM-DD HH:MM:SS): ")
timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

# Parameterized query
query = "INSERT INTO sensor_reading (id, temperature, humidity, timestamp) VALUES (%s, %s, %s, %s)"
data = (id, temperature, humidity, timestamp)

# Execute the query
cursor = connection.cursor()
cursor.execute(query, data)

# Commit changes
connection.commit()

# Close connection
cursor.close()
connection.close()

print("Data inserted successfully into sensor_reading!")

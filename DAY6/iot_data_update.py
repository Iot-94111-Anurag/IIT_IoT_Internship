import mysql.connector

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
id = int(input("Enter the id of the record to update: "))
temperature = float(input("Enter new temperature: "))
humidity = float(input("Enter new humidity: "))

# Parameterized UPDATE query
query = """
    UPDATE sensor_reading
    SET temperature = %s, humidity = %s
    WHERE id = %s
"""
data = (temperature, humidity, id)

# Execute the query
cursor = connection.cursor()
cursor.execute(query, data)

# Commit changes
connection.commit()

# Close connection
cursor.close()
connection.close()

print(f"Record with id={id} updated successfully!")

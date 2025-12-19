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
id_to_delete = int(input("Enter the id of the record to delete: "))

# Parameterized DELETE query
delete_query = "DELETE FROM sensor_reading WHERE id = %s"
data = (id_to_delete,)

# Execute the query
cursor = connection.cursor()
cursor.execute(delete_query, data)

# Commit changes
connection.commit()

# Close connection
cursor.close()
connection.close()

print(f"Record with id={id_to_delete} deleted successfully!")

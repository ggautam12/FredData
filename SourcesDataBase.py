import csv
import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='rds-mysql-gautamdatabase.c7vtm1ac9mjg.us-west-1.rds.amazonaws.com',
    user='Gautam',
    password='Great$43111',
    database='Fred'
)

# Create a cursor object for executing MySQL commands
cursor = conn.cursor()

# Create the table
cursor.execute(
    """CREATE TABLE sources (
        id VARCHAR(255),
        name VARCHAR(255),
        realtime_start DATE
    )"""
)

# Open the CSV file
with open('sources.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Skip the header row
    next(reader)

    # Iterate over the rows in the CSV file
    for row in reader:
        # Insert the data into the table
        cursor.execute(
            "INSERT INTO sources (id, name, realtime_start) VALUES (%s, %s, %s)",
            (row[0], row[1], row[2])
        )

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

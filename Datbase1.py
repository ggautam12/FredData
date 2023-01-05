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
    """CREATE TABLE categories (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255),
        parent_id INTEGER
    )"""
)

# Open the CSV file
with open('children_categories.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Skip the header row
    next(reader)

    # Iterate over the rows in the CSV file
    for row in reader:
        # Insert the data into the table
        cursor.execute(
            "INSERT INTO categories (id, name, parent_id) VALUES (%s, %s, %s)",
            row
        )

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

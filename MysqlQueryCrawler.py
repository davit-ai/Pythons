import pymysql
import os
import csv

# Database connection details
host = 'your_host'
user = 'your_user'
password = 'your_password'

# Directory to save the files
base_dir = 'D:/'

# Connect to the MySQL server
connection = pymysql.connect(host=host, user=user, password=password)

try:
    with connection.cursor() as cursor:
        # Get the list of databases
        cursor.execute("SHOW DATABASES;")
        databases = cursor.fetchall()

        for db in databases:
            db_name = db[0]

            # Skip system databases
            if db_name in ('information_schema', 'mysql', 'performance_schema', 'sys'):
                continue

            # Create directory for the database
            db_dir = os.path.join(base_dir, db_name)
            os.makedirs(db_dir, exist_ok=True)

            # Connect to the specific database
            connection.select_db(db_name)

            # Get the list of tables
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()

            for table in tables:
                table_name = table[0]

                # We only want to run the query on the 'customer' table
                if table_name == 'customer':
                    query = f"SELECT * FROM {table_name};"
                    cursor.execute(query)
                    rows = cursor.fetchall()

                    # Get column names
                    column_names = [i[0] for i in cursor.description]

                    # Write the output to a CSV file
                    file_path = os.path.join(db_dir, f"{table_name}.csv")
                    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerow(column_names)  # Write header
                        csv_writer.writerows(rows)  # Write data
finally:
    connection.close()

import pyodbc
import os

# Database connection parameters
db_params = {
'server': 'MTVT-DAVITKHANA',
'database': 'MMREMIT_SIT',
'username': 'MTVT-DAVITKHANA\V-Tech'
}

# Connection string
conn_str = (
f"DRIVER={{ODBC Driver 17 for SQL Server}};"
f"SERVER={db_params['server']};"
f"DATABASE={db_params['database']};"
f"UID={db_params['username']};"
f"Trusted_Connection=yes;"
)

# Connect to the database
connection = pyodbc.connect(conn_str)
cursor = connection.cursor()

# Query to retrieve stored procedure information
proc_query = "SELECT name FROM sys.procedures;"

# Execute the query
cursor.execute(proc_query)

# Fetch all stored procedures
procedures = cursor.fetchall()

# Directory to save the stored procedure definitions
local_dir = "D:\DB_Present\Codes\code output"

# Function to get the definition of the procedure
def get_proc_definition(proc_name):
    cursor.execute(f"EXEC sp_helptext '{proc_name}'")
    return ''.join([row[0] for row in cursor.fetchall()])

# Save the definitions to the local directory
for proc in procedures:
    proc_name = proc[0]
definition = get_proc_definition(proc_name)
file_path = os.path.join(local_dir, f"{proc_name}.sql")

# Write the definition to a file
with open(file_path, "w") as file:
    file.write(definition)

# Close the database connection
cursor.close()
connection.close()

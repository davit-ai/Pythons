import psycopg2
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname='plane',
            user='postgres',
            password='root',
            host='localhost',
            port='5432'
        )
        print("Database Connected")
        return conn
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def check_connection():
    conn = connect_to_db()
    if conn:
        print("Database connection is successful.")
        conn.close()
    else:
        print("Failed to connect to the database.")

# Call the check_connection function to test the database connection
check_connection()

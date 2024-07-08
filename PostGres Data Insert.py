import psycopg2
from psycopg2 import sql


# Function to connect to the PostgreSQL database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname='plane',
            user='postgres',
            password='root',
            host='localhost',
            port='5432'
        )
        return conn
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


# Function to insert data into the database
def insert_data(name, email):
    conn = connect_to_db()
    if conn is not None:
        try:
            with conn.cursor() as cur:
                cur.execute(sql.SQL("""
                    INSERT INTO public.employee(
                        created_at, updated_at, id, name, email)
                    VALUES (NOW(), NOW(), gen_random_uuid(), %s, %s);
                """), (name, email))
            conn.commit()
            print("Data inserted successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
    else:
        print("Connection to database failed.")


# Main function to take input and call the insert function
def main():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    insert_data(name, email)


if __name__ == "__main__":
    main()

import psycopg

# Connect to an existing database
with psycopg.connect("dbname=test",
                     "host=localhost",
                     "user=postgres",
                     "password=postgres"
                     "port=5432"
                     ) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM test")
        print(cur.fetchall())

cur.execute("SELECT * from portal.portal_users;")

# Fetch all rows from database
record = cur.fetchall()

print("Data from Database:- ", record)
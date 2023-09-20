import psycopg2

conn = psycopg2.connect(
    host="project1.ciei3rbunefb.us-west-1.rds.amazonaws.com",
    database="postgres",
    user="project1_db",
    password="project1dbpass",
    port="5432")

cursor = conn.cursor()
cursor.execute("SELECT * FROM information_schema.tables")
rows = cursor.fetchall()
for table in rows:
    print(table)
conn.close()

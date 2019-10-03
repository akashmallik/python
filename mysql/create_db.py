import mysql.connector as sql

db = sql.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)
print(db)

cursor = db.cursor()
# cursor.execute("CREATE DATABASE pysql")
cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)
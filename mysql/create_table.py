import mysql.connector as sql

db = sql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "pysql"
)
print(db)

cursor = db.cursor()
# cursor.execute("SHOW DATABASES")

# for x in cursor:
#     print(x)

# cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# cursor.execute("SHOW TABLES")
# print(cursor)

# for x in cursor:
#     print(x)

# cursor.execute("CREATE TABLE test (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
cursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# Important!: Notice the statement: mdb.commit(). It is required to make the changes, otherwise no changes are made to the table.

import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "pysql"
)
print(db)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Akash Mallik", "Dhaka, Bangladesh") # single
# cursor.execute(sql,val)
val = [
        ('Arif', 'Dhaka, Bangladesh'),
        ('Lima', 'Dhaka, Bangladesh'),
        ('Titu', 'Mymonshing'),
    ] # multiple data
cursor.executemany(sql,val)

db.commit()
print(cursor.rowcount, "record inserted")
print("1 record inserted, ID:", cursor.lastrowid) # last inserted id

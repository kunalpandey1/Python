import sqlite3

connection = sqlite3.connect("users.db")

cursor = connection.cursor()

cursor.execute("INSERT INTO users VALUES ('Kunal','12345678','22')")
cursor.execute("INSERT INTO users VALUES ('Rishab','12345678','45')")
cursor.execute("INSERT INTO users VALUES ('Joshua','12345678','99')")


connection.commit()

connection.close()

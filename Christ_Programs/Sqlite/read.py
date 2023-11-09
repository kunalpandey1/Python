import sqlite3

connection = sqlite3.connect("users.db")

cursor = connection.cursor()


cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
print(users)

for user in users:
    print(user)

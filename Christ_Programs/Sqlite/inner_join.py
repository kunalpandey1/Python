import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create the tables
c.execute('''CREATE TABLE IF NOT EXISTS user
             (user_id INTEGER PRIMARY KEY, name text, age integer)''')

c.execute('''CREATE TABLE IF NOT EXISTS orders
             (order_id INTEGER PRIMARY KEY, user_id INTEGER,
              FOREIGN KEY(user_id) REFERENCES user(user_id))''')

# Insert some sample data
c.execute("INSERT INTO user (name, age) VALUES ('Alice', 30)")
c.execute("INSERT INTO user (name, age) VALUES ('Bob', 25)")
c.execute("INSERT INTO orders (user_id) VALUES (1)")
c.execute("INSERT INTO orders (user_id) VALUES (2)")

# Commit the changes
conn.commit()

c.execute("SELECT * FROM orders")
order = c.fetchall()
c.execute("SELECT * FROM user")
user = c.fetchall()

for u in user:
    print(user)

for o in order:
    print(order)    


# Perform an inner join query
c.execute('''SELECT user.name, user.age, orders.order_id
             FROM user
             INNER JOIN orders ON user.user_id = orders.user_id''')

# Fetch the results
results = c.fetchall()
for row in results:
    print(row)

# Close the connection
conn.close()

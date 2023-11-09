import sqlite3

# Create a new database (if it doesn't exist) and establish a connection
conn = sqlite3.connect("grocery_store.db")
cursor = conn.cursor()

# Retrieve data from the Products table
cursor.execute('''
    SELECT Products.name, Products.price
    FROM Products
''')

products = cursor.fetchall()
print("Products:")
for product in products:
    print(product)

# Retrieve data from the Customers table
cursor.execute('''
    SELECT Customers.name, Products.name AS product_name
    FROM Customers
    LEFT JOIN Products ON Customers.id = Products.id
''')
results = cursor.fetchall()
for row in results:
    print(row)

conn.close()

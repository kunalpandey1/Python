import sqlite3

# Create a new database (if it doesn't exist) and establish a connection
conn = sqlite3.connect("grocery_store.db")
cursor = conn.cursor()

# Retrieve data from the Products table
cursor.execute('SELECT * FROM Products')
products = cursor.fetchall()
print("Products:")
for product in products:
    print(product)

# Update a record in the Products table
new_price = 3.5
cursor.execute('UPDATE Products SET price = ? WHERE id = ?', (new_price, 1))
conn.commit()
print(f"Updated price for Apple: {new_price}")

# Retrieve data from the Customers table
cursor.execute('SELECT * FROM Customers')
customers = cursor.fetchall()
print("Customers:")
for customer in customers:
    print(customer)

# Delete a record from the Customers table
cursor.execute('DELETE FROM Customers WHERE id = ?', (1,))
conn.commit()
print("Deleted John Doe from Customers")

# Close the connection
conn.close()

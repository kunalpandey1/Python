import sqlite3

# Create a new database (if it doesn't exist) and establish a connection
conn = sqlite3.connect("grocery_store.db")
cursor = conn.cursor()

# Create the Products table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL
    )
''')

# Create the Customers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Insert sample data into the Products table
products_data = [
    ('Apple', 'Fruits', 2.5),
    ('Banana', 'Fruits', 1.5),
    ('Carrot', 'Vegetables', 1.0),
    ('Broccoli', 'Vegetables', 2.0),
    ('Milk', 'Dairy', 3.0),
    ('Yogurt', 'Dairy', 2.0),
    ('Chicken', 'Meat', 5.0),
    ('Beef', 'Meat', 7.0),
    ('Soda', 'Beverages', 1.0),
    ('Water', 'Beverages', 0.5),
    ('Chips', 'Snacks', 2.5),
    ('Cookies', 'Snacks', 3.0)
]

cursor.executemany('INSERT INTO Products (name, category, price) VALUES (?, ?, ?)', products_data)

# Insert sample data into the Customers table
customers_data = [
    ('John Doe', 'johndoe@example.com'),
    ('Jane Smith', 'janesmith@example.com'),
    ('Bob Johnson', 'bobjohnson@example.com'),
    ('Alice Brown', 'alicebrown@example.com'),
    ('David Lee', 'davidlee@example.com'),
    ('Emily Davis', 'emilydavis@example.com'),
    ('Michael Wilson', 'michaelwilson@example.com'),
    ('Samantha Taylor', 'samanthataylor@example.com'),
    ('Kevin Anderson', 'kevinanderson@example.com'),
    ('Laura White', 'laurawhite@example.com'),
    ('Matthew Harris', 'matthewharris@example.com'),
    ('Olivia Clark', 'oliviaclark@example.com'),
    ('William Turner', 'williamturner@example.com')
]

cursor.executemany('INSERT INTO Customers (name, email) VALUES (?, ?)', customers_data)

# Commit the changes
conn.commit()

conn.close()

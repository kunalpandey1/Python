# import csv
# import random

# # Generate random grocery data for demonstration
# header = ["Item", "Category", "Price", "Quantity"]
# data = []

# categories = ["Fruits", "Vegetables", "Dairy", "Meat", "Beverages", "Snacks"]

# for i in range(1, 100):
#     item = f"Item{i}"
#     category = random.choice(categories)
#     price = round(random.uniform(0.5, 50), 2)
#     quantity = random.randint(1, 100)
#     data.append([item, category, price, quantity])

# # Save the data to a CSV file
# with open("grocery.csv", mode="w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(header)
#     writer.writerows(data)

import sqlite3
import csv
import random

# Generate random grocery data for demonstration
header = ["Item", "Category", "Price", "Quantity"]
data = []

categories = ["Fruits", "Vegetables", "Dairy", "Meat", "Beverages", "Snacks"]

for i in range(1, 100):
    item = f"Item{i}"
    category = random.choice(categories)
    price = round(random.uniform(0.5, 50), 2)
    quantity = random.randint(1, 100)
    data.append([item, category, price, quantity])

# Save the data to a CSV file
with open("grocery.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

# SQLite CRUD operations
db_file = 'grocery_data.db'
csv_file = 'grocery.csv'


# Function to create a SQLite database and table
def create_table():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS groceries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT,
            category TEXT,
            price REAL,
            quantity INTEGER
        )
    ''')
    conn.commit()
    conn.close()


# Function to insert data from a CSV file into the SQLite database
def insert_data_from_csv():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            cursor.execute('''
                INSERT INTO groceries (item, category, price, quantity) VALUES (?, ?, ?, ?)
            ''', (row[0], row[1], row[2], row[3]))

    conn.commit()
    conn.close()


# Function to read data from the SQLite database
def read_data():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM groceries')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


# Function to update data in the SQLite database
def update_data(id, item, category, price, quantity):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE groceries SET item = ?, category = ?, price = ?, quantity = ? WHERE id = ?
    ''', (item, category, price, quantity, id))

    conn.commit()
    conn.close()


# Function to delete data from the SQLite database
def delete_data(id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM groceries WHERE id = ?', (id,))

    conn.commit()
    conn.close()


# Function to prompt the user for updating an item
def prompt_update_data():
    item_id = input("Enter the ID of the item you want to update: ")
    item_name = input("Enter the new name of the item: ")
    item_category = input("Enter the new category of the item: ")
    item_price = input("Enter the new price of the item: ")
    item_quantity = input("Enter the new quantity of the item: ")

    update_data(item_id, item_name, item_category, item_price, item_quantity)


# Function to prompt the user for deleting an item
def prompt_delete_data():
    item_id = input("Enter the ID of the item you want to delete: ")

    delete_data(item_id)


# Main function
if __name__ == '__main__':
    create_table()
    insert_data_from_csv()
    read_data()

    # Example usage of update and delete functions
    prompt_update_data()
    prompt_delete_data()

    # Read the data after the update and delete operations
    read_data()

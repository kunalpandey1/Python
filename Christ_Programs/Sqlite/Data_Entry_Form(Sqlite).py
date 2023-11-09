import tkinter as tk
from tkinter import ttk
import sqlite3

# Create database or connect to one
conn = sqlite3.connect('registration.db')
# Create cursor
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS registrations (
             id INTEGER PRIMARY KEY,
             first_name text NOT NULL,
             last_name text NOT NULL,
             email text NOT NULL
             )''')
# Commit changes
conn.commit()

def insert_data():
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()
    c.execute("INSERT INTO registrations VALUES (:id, :first_name, :last_name, :email)",
              {
                  'id': None,
                  'first_name': first_name.get(),
                  'last_name': last_name.get(),
                  'email': email.get()
              })
    conn.commit()
    conn.close()
    view_data()

def delete_data():
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()
    c.execute("DELETE FROM registrations WHERE id = " + selected_id.get())
    conn.commit()
    conn.close()
    view_data()

def update_data():
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()
    c.execute("""UPDATE registrations SET
            first_name = :first,
            last_name = :last,
            email = :email
            WHERE id = :id""",
              {
                  'first': first_name_editor.get(),
                  'last': last_name_editor.get(),
                  'email': email_editor.get(),
                  'id': selected_id.get()
              })
    conn.commit()
    conn.close()
    editor.destroy()
    view_data()

def edit_data():
    global editor
    editor = tk.Tk()
    editor.title('Update a Record')

    conn = sqlite3.connect('registration.db')
    c = conn.cursor()
    c.execute("SELECT * FROM registrations WHERE id=" + selected_id.get())
    records = c.fetchall()

    global first_name_editor
    global last_name_editor
    global email_editor
    # Create Text Boxes
    first_name_editor = tk.Entry(editor, width=30)
    first_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    last_name_editor = tk.Entry(editor, width=30)
    last_name_editor.grid(row=1, column=1)
    email_editor = tk.Entry(editor, width=30)
    email_editor.grid(row=2, column=1)

    # Create Text Box Labels
    first_name_label = tk.Label(editor, text="First Name")
    first_name_label.grid(row=0, column=0, pady=(10, 0))
    last_name_label = tk.Label(editor, text="Last Name")
    last_name_label.grid(row=1, column=0)
    email_label = tk.Label(editor, text="Email")
    email_label.grid(row=2, column=0)

    for record in records:
        first_name_editor.insert(0, record[1])
        last_name_editor.insert(0, record[2])
        email_editor.insert(0, record[3])

    edit_btn = tk.Button(editor, text="Save Record", command=update_data)
    edit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

def view_data():
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()
    c.execute("SELECT * FROM registrations")
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = tk.Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()

root = tk.Tk()
root.title('Registration Form')

# Create Text Boxes
first_name = tk.Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20, pady=(10, 0))
last_name = tk.Entry(root, width=30)
last_name.grid(row=1, column=1)
email = tk.Entry(root, width=30)
email.grid(row=2, column=1)

selected_id = tk.Entry(root, width=30)
selected_id.grid(row=10, column=1)

# Create Text Box Labels
first_name_label = tk.Label(root, text="First Name")
first_name_label.grid(row=0, column=0, pady=(10, 0))
last_name_label = tk.Label(root, text="Last Name")
last_name_label.grid(row=1, column=0)
email_label = tk.Label(root, text="Email")
email_label.grid(row=2, column=0)
id_label = tk.Label(root, text="Select ID")
id_label.grid(row=10, column=0)

# Create Submit Button
submit_btn = tk.Button(root, text="Add Record to Database", command=insert_data)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = tk.Button(root, text="Show Records", command=view_data)
query_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a Delete Button
delete_btn = tk.Button(root, text="Delete Record", command=delete_data)
delete_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an Update Button
edit_btn = tk.Button(root, text="Update Record", command=edit_data)
edit_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

conn.close()

root.mainloop()

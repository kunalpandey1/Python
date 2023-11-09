import tkinter as tk
import re

def validate_email(email):
    # Regular expression for a simple email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def validate_password(password):
    # Regular expression for password strength: at least 8 characters, one uppercase letter, one lowercase letter, and one digit
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
    return re.match(pattern, password)

def register():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not validate_email(email):
        status_label.config(text="Invalid email format", fg="red")
    elif not validate_password(password):
        status_label.config(text="Weak password", fg="red")
    else:
        # Registration logic here (you can save the data to a file or a database)
        status_label.config(text="Registration successful", fg="green")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place form elements
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Show asterisks for password
password_entry.pack()

register_button = tk.Button(root, text="Register", command=register)
register_button.pack()

status_label = tk.Label(root, text="", fg="green")
status_label.pack()

# Start the Tkinter main loop
root.mainloop()

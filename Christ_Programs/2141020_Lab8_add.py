import tkinter as tk
import tkinter.messagebox as messagebox
import re

# Function to go back to the homepage and reset button visibility
def go_to_homepage():
    buying_grocery_frame.pack_forget()
    homepage_frame.pack()
    show_buttons()

# Function to hide buttons
def hide_buttons():
    buy_button.pack_forget()
    remove_button.grid_forget()
    search_button.grid_forget()

# Function to show buttons
def show_buttons():
    buy_button.pack(pady=10)
    remove_button.grid(row=1, column=0, pady=10)
    search_button.grid(row=2, column=0, pady=10)

# Function to calculate the total amount and display it
def calculate_total():
    grocery_name = grocery_name_entry.get()
    grocery_price = grocery_price_entry.get()
    grocery_quantity = grocery_quantity_entry.get()
    
    # Regular expressions for validation
    name_pattern = r"^[A-Za-z\s]+$"  # Only characters and spaces allowed
    price_pattern = r"^\d+(\.\d{1,2})?$"  # Valid price is a positive float with up to 2 decimal places
    quantity_pattern = r"^\d+$"  # Valid quantity is a positive integer
    
    if not re.match(name_pattern, grocery_name):
        messagebox.showerror("Error", "Invalid Grocery Name")
    elif not re.match(price_pattern, grocery_price):
        messagebox.showerror("Error", "Invalid Grocery Price")
    elif not re.match(quantity_pattern, grocery_quantity):
        messagebox.showerror("Error", "Invalid Grocery Quantity")
    else:
        total_amount = float(grocery_price) * int(grocery_quantity)
        messagebox.showinfo("Total Amount", f"Total Amount: ${total_amount:.2f}")
        go_to_homepage()

root = tk.Tk()
root.title("Grocery Management System")
root.geometry("400x300")
root.configure(bg="black")

homepage_frame = tk.Frame(root, bg="black")
homepage_frame.pack()

homepage_title_label = tk.Label(homepage_frame, text="Grocery Management", font=("Helvetica", 20, "bold"), fg="white", bg="black")
homepage_title_label.pack(pady=20)

button_frame = tk.Frame(root, bg="black")
button_frame.pack()

buy_button = tk.Button(homepage_frame, text="BUYING GROCERY", font=("Helvetica", 12, "bold"), fg="red", bg="black", relief="ridge",
                       command=lambda: [homepage_frame.pack_forget(), buying_grocery_frame.pack(), hide_buttons()])
remove_button = tk.Button(button_frame, text="REMOVE GROCERY", font=("Helvetica", 12, "bold"), fg="blue", bg="black", relief="ridge")
search_button = tk.Button(button_frame, text="SEARCH GROCERY", font=("Helvetica", 12, "bold"), fg="orange", bg="black", relief="ridge")
buy_button.pack(pady=10)
remove_button.grid(row=1, column=0, pady=10)
search_button.grid(row=2, column=0, pady=10)

buying_grocery_frame = tk.Frame(root, bg="black")

buying_grocery_title_label = tk.Label(buying_grocery_frame, text="BUYING GROCERY", font=("Helvetica", 16, "bold"), fg="white", bg="black")
buying_grocery_title_label.pack(pady=10)

grocery_name_label = tk.Label(buying_grocery_frame, text="Grocery Name:", font=("Helvetica", 12, "bold"), fg="white", bg="black")
grocery_name_label.pack()
grocery_name_entry = tk.Entry(buying_grocery_frame, font=("Helvetica", 12))
grocery_name_entry.pack(pady=5)

grocery_price_label = tk.Label(buying_grocery_frame, text="Grocery Price:", font=("Helvetica", 12, "bold"), fg="white", bg="black")
grocery_price_label.pack()
grocery_price_entry = tk.Entry(buying_grocery_frame, font=("Helvetica", 12))
grocery_price_entry.pack(pady=5)

grocery_quantity_label = tk.Label(buying_grocery_frame, text="Grocery Quantity:", font=("Helvetica", 12, "bold"), fg="white", bg="black")
grocery_quantity_label.pack()
grocery_quantity_entry = tk.Entry(buying_grocery_frame, font=("Helvetica", 12))
grocery_quantity_entry.pack(pady=5)

submit_button = tk.Button(buying_grocery_frame, text="Submit", font=("Helvetica", 12, "bold"), fg="green", bg="black", relief="ridge",
                          command=calculate_total)
submit_button.pack(pady=10)

back_button = tk.Button(buying_grocery_frame, text="Back to Homepage", font=("Helvetica", 12, "bold"), fg="blue", bg="black", relief="ridge",
                        command=go_to_homepage)
back_button.pack(pady=10)

root.mainloop()

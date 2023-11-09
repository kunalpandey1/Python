import tkinter as tk
from tkinter import messagebox

# Function to calculate the result and save data to a text file
def calculate_and_save():
    grocery_name = grocery_name_entry.get()
    price = float(price_entry.get())
    quantity = int(quantity_entry.get())
    
    result = price * quantity
    
    # Display the result
    result_label.config(text=f"Result: {result}")
    
    # Save data to a text file
    with open("grocery_data.txt", "a") as file:
        file.write(f"Grocery Name: {grocery_name}\n")
        file.write(f"Price: {price}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Result: {result}\n\n")
    
    messagebox.showinfo("Info", "Data saved successfully.")

# Create the main window
root = tk.Tk()
root.title("Grocery Calculator")

# Grocery Name Input
grocery_name_label = tk.Label(root, text="Grocery Name:")
grocery_name_label.pack()
grocery_name_entry = tk.Entry(root)
grocery_name_entry.pack()

# Price Input
price_label = tk.Label(root, text="Price:")
price_label.pack()
price_entry = tk.Entry(root)
price_entry.pack()

# Quantity Input
quantity_label = tk.Label(root, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_and_save)
calculate_button.pack()

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()

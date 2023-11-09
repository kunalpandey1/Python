import tkinter as tk

# Function to update the display
def update_display(value):
    current_text = display.get()
    if current_text == "0":
        display.set(value)
    else:
        display.set(current_text + value)

# Function to clear the display
def clear_display():
    display.set("0")

# Function to perform calculations
def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.set(result)
    except Exception as e:
        display.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and place the display
display = tk.StringVar()
display.set("0")
display_entry = tk.Entry(root, textvariable=display, font=("Arial", 20), bd=10, insertwidth=4, width=14, justify="right")
display_entry.grid(row=0, column=0, columnspan=4)

# Create and place the buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=lambda b=button: update_display(b) if b not in {"=", "C"} else calculate() if b == "=" else clear_display()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the Tkinter main loop
root.mainloop()

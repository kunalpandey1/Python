import tkinter as tk

from tkinter import messagebox

import csv

 

def display_register_number():

    messagebox.showinfo("Register Number", "My Register Number is ")

 

def display_name():

    messagebox.showinfo("Name", "My name is ")

 

def exit_program():

    root.destroy()

 

def load_data_from_csv():

    data = []

 

    try:

        with open('iris.csv', 'r') as file:

            csv_reader = csv.reader(file)

           

            for row in csv_reader:

                data.append(row)

 

    except FileNotFoundError:

        messagebox.showerror("Error!", 'iris.csv file not found!')

 

    return data

 

def create_table(data):

    for i, row in enumerate(data):

        for j, value in enumerate(row):

            cell = tk.Label(frame, text = value, padx=10, pady=5, borderwidth=1, relief="solid")

            cell.grid(row = i, column= j)

 

root = tk.Tk()

root.title("Table Display with the MenuBar")

 

menubar = tk.Menu(root)

 

file_menu = tk.Menu(menubar, tearoff=0)

file_menu.add_command(label="Exit", command=exit_program)

 

display_menu = tk.Menu(menubar, tearoff=0)

display_menu.add_command(label="Register Number", command=display_register_number)

display_menu.add_command(label="Name", command=display_name)

 

menubar.add_cascade(label="File", menu=file_menu)

menubar.add_cascade(label="Display", menu=display_menu)

 

root.config(menu=menubar)

 

data = load_data_from_csv()

 

frame = tk.Frame(root)

frame.pack()

 

create_table(data)

 

root.mainloop()

 
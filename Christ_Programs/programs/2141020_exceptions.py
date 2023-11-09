import tkinter as tk
from tkinter import messagebox

class GroceryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery Management System")
        
        self.grocery_list = []
        
        self.item_label = tk.Label(root, text="Item:")
        self.item_label.pack()
        self.item_entry = tk.Entry(root)
        self.item_entry.pack()
        
        self.quantity_label = tk.Label(root, text="Quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.pack()
        
        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack()
        
        self.view_button = tk.Button(root, text="View List", command=self.view_list)
        self.view_button.pack()
        
        self.delete_button = tk.Button(root, text="Delete Item", command=self.delete_item)
        self.delete_button.pack()
        
    def add_item(self):
        try:
            item = self.item_entry.get()
            quantity = int(self.quantity_entry.get())
            
            if quantity <= 0:
                raise ValueError("Quantity must be a positive number")
            
            self.grocery_list.append((item, quantity))
            messagebox.showinfo("Success", f"Added {quantity} {item}(s) to your list.")
            
            self.item_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
    
    def view_list(self):
        if not self.grocery_list:
            messagebox.showinfo("Grocery List", "Your list is empty.")
        else:
            list_text = "\n".join([f"{item}: {quantity}" for item, quantity in self.grocery_list])
            messagebox.showinfo("Grocery List", list_text)
    
    def delete_item(self):
        try:
            item = self.item_entry.get()
            for i, (existing_item, quantity) in enumerate(self.grocery_list):
                if existing_item == item:
                    del self.grocery_list[i]
                    messagebox.showinfo("Success", f"Removed {item} from your list.")
                    self.item_entry.delete(0, tk.END)
                    return
            raise ValueError(f"{item} not found in the list.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryManagementSystem(root)
    root.mainloop()
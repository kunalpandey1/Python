import tkinter as tk
from tkinter import ttk
import json

class CurrencyConverter:
    def __init__(self):
        self.conversion_rates = {
            'USD': {'EUR': 0.85, 'JPY': 110.28, 'GBP': 0.72},
            'EUR': {'USD': 1.18, 'JPY': 128.09, 'GBP': 0.83},
            'JPY': {'USD': 0.0091, 'EUR': 0.0078, 'GBP': 0.0065},
            'GBP': {'USD': 1.39, 'EUR': 1.21, 'JPY': 153.39}
        }
        self.history = []

    def load_conversion_rates(self, filename):
        try:
            with open(filename, 'r') as file:
                self.conversion_rates = json.load(file)
        except FileNotFoundError:
            self.conversion_rates = {}

    def save_conversion_rates(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.conversion_rates, file)

    def convert(self, amount, from_currency, to_currency):
        if from_currency != to_currency:
            rate = self.conversion_rates.get(from_currency, {}).get(to_currency, None)
            if rate is not None:
                converted_amount = amount * rate
                self.history.append((amount, from_currency, converted_amount, to_currency))
                return converted_amount
            else:
                return "Conversion rate not available."
        else:
            return amount

    def undo_conversion(self):
        if self.history:
            self.history.pop()

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        
        self.converter = CurrencyConverter()

        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()
        self.result_var = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Dropdowns for selecting currencies
        from_currency_label = tk.Label(self.root, text="From Currency:")
        from_currency_label.grid(row=0, column=0)
        
        to_currency_label = tk.Label(self.root, text="To Currency:")
        to_currency_label.grid(row=1, column=0)
        
        from_currency_dropdown = ttk.Combobox(self.root, textvariable=self.from_currency_var, values=list(self.converter.conversion_rates.keys()))
        from_currency_dropdown.grid(row=0, column=1)
        
        to_currency_dropdown = ttk.Combobox(self.root, textvariable=self.to_currency_var, values=list(self.converter.conversion_rates.keys()))
        to_currency_dropdown.grid(row=1, column=1)
        
        # Entry for entering the amount
        amount_label = tk.Label(self.root, text="Amount:")
        amount_label.grid(row=2, column=0)
        
        amount_entry = tk.Entry(self.root, textvariable=self.amount_var)
        amount_entry.grid(row=2, column=1)
        
        # Convert button
        convert_button = tk.Button(self.root, text="Convert", command=self.convert)
        convert_button.grid(row=3, column=0, columnspan=2)
        
        # Undo button
        undo_button = tk.Button(self.root, text="Undo", command=self.undo)
        undo_button.grid(row=5, column=0, columnspan=2)
        
        # Result label
        result_label = tk.Label(self.root, text="Result:")
        result_label.grid(row=4, column=0)
        
        result_display = tk.Label(self.root, textvariable=self.result_var)
        result_display.grid(row=4, column=1)
        
    def convert(self):
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        amount = self.amount_var.get()
        
        result = self.converter.convert(amount, from_currency, to_currency)
        self.result_var.set(result)
    
    def undo(self):
        self.converter.undo_conversion()
        self.result_var.set("Conversion undone.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()

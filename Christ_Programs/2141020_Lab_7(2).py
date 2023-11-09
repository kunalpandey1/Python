import re

# Define an abstract base class for grocery items
class GroceryItem:
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price

    def calculate_cost(self, quantity):
        pass  # To be overridden in concrete classes

    def __str__(self):
        return f"{self.item_name}: ₹{self.price:.2f}"

# Define a concrete class for standard grocery items
class StandardGroceryItem(GroceryItem):
    def calculate_cost(self, quantity):
        return self.price * quantity

# Define a concrete class for weighted grocery items
class WeightedGroceryItem(GroceryItem):
    def calculate_cost(self, weight):
        return self.price * weight

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

class GroceryShopping:
    def __init__(self):
        self.shopping_list = []
        self.item_stack = Stack()  # Stack to store items

    def add_item(self):
        item_name = input("Enter the item name: ")
        price = self.get_valid_input("Enter the price per unit: ", float)
        item_type = input("Enter the item type (standard/weighted): ").strip().lower()

        if item_type == "standard":
            quantity = self.get_valid_input("Enter the quantity: ", float)
            item = StandardGroceryItem(item_name, price)
        elif item_type == "weighted":
            weight = self.get_valid_input("Enter the weight in kilograms: ", float)
            item = WeightedGroceryItem(item_name, price)
        else:
            print("Invalid item type. Please enter 'standard' or 'weighted'.")
            return

        self.shopping_list.append((item, item_type))
        self.item_stack.push(item)  # Push the item onto the stack
        print(f"{item_type.capitalize()} {item_name} added to the shopping list.")

    def get_valid_input(self, prompt, data_type):
        while True:
            user_input = input(prompt)
            if re.match(r'^[0-9]*(\.[0-9]+)?$', user_input):
                return data_type(user_input)
            else:
                print("Invalid input. Please enter a valid number.")

    def view_list(self):
        if not self.shopping_list:
            print("Shopping list is empty.")
        else:
            print("Shopping List:")
            total_bill = 0
            for item, item_type in self.shopping_list:
                item_name, price = item.item_name, item.price
                if item_type == "standard":
                    quantity = self.get_quantity_by_item_name(item_name)
                    total_cost = item.calculate_cost(quantity)
                    print(f"{item_name}: {quantity} x ₹{price:.2f} = ₹{total_cost:.2f}")
                    total_bill += total_cost
                elif item_type == "weighted":
                    weight = self.get_weight_by_item_name(item_name)
                    total_cost = item.calculate_cost(weight)
                    print(f"{item_name}: {weight} kg x ₹{price:.2f} = ₹{total_cost:.2f}")
                    total_bill += total_cost

            print(f"Total bill: ₹{total_bill:.2f}")

    def remove_item(self):
        item_name = input("Enter the item name to remove: ")
        found_item = False

        for item, item_type in self.shopping_list:
            if item.item_name.lower() == item_name.lower():
                self.shopping_list.remove((item, item_type))
                self.item_stack.pop()  # Pop the item from the stack
                found_item = True
                print(f"{item.item_name} removed from the shopping list.")
                break

        if not found_item:
            print(f"{item_name} not found in the shopping list.")

    def get_quantity_by_item_name(self, item_name):
        # Assume a standard item with the same name exists in the stack
        for item in self.item_stack.items[::-1]:
            if isinstance(item, StandardGroceryItem) and item.item_name.lower() == item_name.lower():
                return self.shopping_list[self.item_stack.items.index(item)][0]

    def get_weight_by_item_name(self, item_name):
        # Assume a weighted item with the same name exists in the stack
        for item in self.item_stack.items[::-1]:
            if isinstance(item, WeightedGroceryItem) and item.item_name.lower() == item_name.lower():
                return self.shopping_list[self.item_stack.items.index(item)][0]

    def sequential_search(self):
        item_name = input("Enter the item name to search: ").lower()
        found_item = False
        for item, item_type in self.shopping_list:
            if item.item_name.lower() == item_name.lower():
                price = item.price
                if item_type == "standard":
                    quantity = self.get_quantity_by_item_name(item_name)
                    total_cost = item.calculate_cost(quantity)
                    print(f"{item_name}: {quantity} x ₹{price:.2f} = ₹{total_cost:.2f}")
                    found_item = True
                    break
                elif item_type == "weighted":
                    weight = self.get_weight_by_item_name(item_name)
                    total_cost = item.calculate_cost(weight)
                    print(f"{item_name}: {weight} kg x ₹{price:.2f} = ₹{total_cost:.2f}")
                    found_item = True
                    break

        if not found_item:
            print(f"{item_name.capitalize()} not found in the shopping list.")

def main():
    shopping = GroceryShopping()

    while True:
        print("\nGrocery Shopping Menu:")
        print("1. Add item to the shopping list")
        print("2. View the shopping list")
        print("3. Remove item from the shopping list")
        print("4. Calculate total bill")
        print("5. Sequential Search")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            shopping.add_item()
        elif choice == "2":
            shopping.view_list()
        elif choice == "3":
            shopping.remove_item()
        elif choice == "4":
            shopping.view_list()
        elif choice == "5":
            shopping.sequential_search()
        elif choice == "6":
            sort_key = input("Sort by (price/quantity): ").lower()
            if sort_key in ["price", "quantity"]:
                shopping.selection_sort(sort_key)
                print("Shopping list sorted by", sort_key)
            else:
                print("Invalid sort key. Please enter 'price' or 'quantity'.")
        elif choice == "7":
            print("Thank you for using the grocery shopping program. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


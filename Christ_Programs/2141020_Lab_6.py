import re

class GroceryShopping:
    def __init__(self):
        self.shopping_list = []  # List of tuples: ((item_name, price), quantity)

    def add_item(self):
        item_name = input("Enter the item name: ")
        quantity = self.get_valid_input("Enter the quantity: ", int)
        price = self.get_valid_input("Enter the price per unit: ", float)

        item = (item_name, price)  # creating a tuple named item
        self.shopping_list.append((item, quantity))
        print(f"{quantity} {item_name}(s) added to the shopping list.")

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
            for item, quantity in self.shopping_list:
                item_name, price = item
                total_cost = price * quantity
                print(f"{item_name}: {quantity} x ₹{price:.2f} = ₹{total_cost:.2f}")
                total_bill += total_cost
            print(f"Total bill: ₹{total_bill:.2f}")

    def remove_item(self):
        item_name = input("Enter the item name to remove: ")
        found_item = False

        for item in self.shopping_list:
            item_info, _ = item
            name, _ = item_info

            if name.lower() == item_name.lower():
                self.shopping_list.remove(item)
                found_item = True
                print(f"{name} removed from the shopping list.")
                break

        if not found_item:
            print(f"{item_name} not found in the shopping list.")

    def sequential_search(self):
        item_name = input("Enter the item name to search: ").lower()
        found_item = False
        for item, quantity in self.shopping_list:
            item_name_in_list, price = item
            if item_name_in_list.lower() == item_name:
                print(f"{item_name_in_list}: {quantity} x ₹{price:.2f}")
                found_item = True
                break

        if not found_item:
            print(f"{item_name.capitalize()} not found in the shopping list.")


class SelectionSortGrocery(GroceryShopping):
    def selection_sort(self, key):
        n = len(self.shopping_list)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                item_i, quantity_i = self.shopping_list[i]
                item_j, quantity_j = self.shopping_list[j]
                if key == "price":
                    value_i = item_i[1]
                    value_j = item_j[1]
                elif key == "quantity":
                    value_i = quantity_i
                    value_j = quantity_j

                if value_j < value_i:
                    min_index = j
            if min_index != i:
                self.shopping_list[i], self.shopping_list[min_index] = self.shopping_list[min_index], self.shopping_list[i]


def main():
    shopping = SelectionSortGrocery()  # Create an instance of the derived class

    while True:
        print("\nGrocery Shopping Menu:")
        print("1. Add item to the shopping list")
        print("2. View the shopping list")
        print("3. Remove item from the shopping list")
        print("4. Calculate total bill")
        print("5. Sequential Search")
        print("6. Sort the shopping list")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            shopping.add_item()
        elif choice == "2":
            shopping.view_list()
        elif choice == "3":
            shopping.remove_item()
        elif choice == "4":
            shopping.view_list()  # Calculate total bill is same as viewing the list
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

class GroceryShopping:
    def __init__(self):
        self.shopping_list = []  # List of tuples: ((item_name, price), quantity)

    def add_item(self):
        item_name = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price per unit: "))

        item = (item_name, price)  # creating a tuple named item
        self.shopping_list.append((item, quantity))
        print(f"{quantity} {item_name}(s) added to the shopping list.")

    def view_list(self):
        if not self.shopping_list:
            print("Shopping list is empty.")
        else:
            print("Shopping List:")
            total_bill = 0
            for item, quantity in self.shopping_list:
                item_name, price = item  # unpacking the item name and price from a tuple item
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


# Main program
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
            shopping.sequential_search()
        elif choice == "5":
            shopping.sequential_search()
        elif choice == "6":
            print("Thank you for using the grocery shopping program. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

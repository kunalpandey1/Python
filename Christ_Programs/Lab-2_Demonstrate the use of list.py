# Grocery shopping program

# Function to add items to the shopping list
def add_item(shopping_list):
    item_name = input("Enter the item name: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price per unit: "))

    item = (item_name, price) # creating a tuple named item
    shopping_list.append((item, quantity))
    print(f"{quantity} {item_name}(s) added to the shopping list.")

# Function to view the shopping list
def view_list(shopping_list):
    if not shopping_list:
        print("Shopping list is empty.")
    else:
        print("Shopping List:")
        total_bill = 0
        for item, quantity in shopping_list:
            item_name, price = item # unpacking the item name and price from a tuple item
            total_cost = price * quantity
            print(f"{item_name}: {quantity} x ₹{price:.2f} = ₹{total_cost:.2f}")
            total_quantity = sum(q for _, q in shopping_list) 
            print(f"Total Quantity of items Purchased: {total_quantity}")
            total_bill += total_cost
        print(f"Total bill: ₹{total_bill:.2f}")

# Function to remove an item from the shopping list
#the variable "_" is used as a placeholder for a value that the code doesn't require. It's a common convention in Python to use "_" as a variable name when you need to unpack a tuple, but you are only interested in certain elements of the tuple and want to ignore the rest.
def remove_item(shopping_list):
    item_name = input("Enter the item name to remove: ")
    found_item = False

    for item in shopping_list:
        item_info, _ = item
        name, _ = item_info
        
        if name.lower() == item_name.lower():
            shopping_list.remove(item)
            found_item = True
            print(f"{name} removed from the shopping list.")
            break

    if not found_item:
        print(f"{item_name} not found in the shopping list.")

def sequential_search(shopping_list):
    item_name = input("Enter the item name to search: ").lower()
    found_item = False
    for item, quantity in shopping_list:
        item_name_in_list, price = item
        if item_name_in_list.lower() == item_name:
            print(f"{item_name_in_list}: {quantity} x ₹{price:.2f}")
            print("found")
            found_item = True
            break

    if not found_item:
        print(f"{item_name.capitalize()} not found in the shopping list.")

# Additional function to demonstrate tuple operations
def demonstrate_tuple_operations():
    # Sample tuples for product information (name, price, quantity)
    product1 = input("Enter product name, price, and quantity (separated by commas): ").split(',')
    product1 = (product1[0].strip(), float(product1[1].strip()), int(product1[2].strip()))

    product2 = input("Enter product name, price, and quantity (separated by commas): ").split(',')
    product2 = (product2[0].strip(), float(product2[1].strip()), int(product2[2].strip()))

    product3 = input("Enter product name, price, and quantity (separated by commas): ").split(',')
    product3 = (product3[0].strip(), float(product3[1].strip()), int(product3[2].strip()))

    # Packing multiple product information in a list
    shopping_list = [product1, product2, product3]

    # Unpacking and displaying product information
    print("\nTuple Operations:")
    for product in shopping_list:
        name, price, quantity = product
        total_cost = price * quantity
        print(f"{name}: {quantity} x ₹{price:.2f} = ₹{total_cost:.2f}")

       

# Main program
def main():
    shopping_list = []  # List of tuples: ((item_name, price), quantity)

    while True:
        print("\nGrocery Shopping Menu:")
        print("1. Add item to the shopping list")
        print("2. View the shopping list")
        print("3. Remove item from the shopping list")
        print("4. Calculate total bill")
        print("5. Demonstrate Tuple Operations")  # New option for tuple operations
        print("6. Sequential Search")
        print("7. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            view_list(shopping_list)
        elif choice == "3":
            remove_item(shopping_list)
        elif choice == "4":
            view_list(shopping_list)
        elif choice == "5":
            demonstrate_tuple_operations()  # Call the tuple operations function
        elif choice == "6":
            sequential_search(shopping_list) 
        elif choice == "7":
            print("Thank you for using the grocery shopping program. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
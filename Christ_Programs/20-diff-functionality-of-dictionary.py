# Initializing a grocery dictionary
grocery_items = {
    'apple': 5,
    'banana': 6,
    'chocolate': 3,
    'milk': 2,
    'bread': 4
}

# 1. Accessing an item's quantity
print("Quantity of apples:", grocery_items['apple'])

# 2. Adding a new item
grocery_items['eggs'] = 12
print("Updated grocery list:", grocery_items)

# 3. Modifying an item's quantity
grocery_items['milk'] = 3
print("Modified grocery list:", grocery_items)

# 4. Removing an item
if 'chocolate' in grocery_items:
    del grocery_items['chocolate']
print("Grocery list after removing chocolate:", grocery_items)

# 5. Check if an item exists
if 'banana' in grocery_items:
    print("Yes, banana is in the grocery list.")

# 6. Get all the keys
print("All items in the grocery list:", grocery_items.keys())

# 7. Get all the values
print("Quantities in the grocery list:", grocery_items.values())

# 8. Get all the key-value pairs
print("All items and quantities in the grocery list:", grocery_items.items())

# 9. Check the length of the dictionary
print("Number of items in the grocery list:", len(grocery_items))

# 10. Copying a dictionary
grocery_items_copy = grocery_items.copy()
print("Copy of the grocery list:", grocery_items_copy)

# 11. Clearing the dictionary
grocery_items.clear()
print("Cleared grocery list:", grocery_items)

# 12. Using get() method to retrieve value
quantity = grocery_items_copy.get('banana')
print("Quantity of bananas using get method:", quantity)

# 13. Using pop() method to remove an item
removed_item = grocery_items_copy.pop('banana')
print("Removed item:", removed_item)

# 14. Using setdefault() method to add an item if it doesn't exist
grocery_items_copy.setdefault('chips', 5)
print("Grocery list with chips added:", grocery_items_copy)

# 15. Using update() method to merge dictionaries
new_items = {'cookies': 2, 'soda': 4}
grocery_items_copy.update(new_items)
print("Merged grocery list:", grocery_items_copy)

# 16. Iterating through keys and values
for item in grocery_items_copy:
    print(f"Item: {item}, Quantity: {grocery_items_copy[item]}")

# 17. Iterating through key-value pairs
for item, quantity in grocery_items_copy.items():
    print(f"Item: {item}, Quantity: {quantity}")

# 18. Creating a nested dictionary
nested_dict = {
    'fruits': {'apple': 5, 'banana': 6},
    'dairy': {'milk': 2, 'cheese': 3}
}

# 19. Check if dictionary is empty
print("Is grocery_items dictionary empty?", not bool(grocery_items_copy))

# 20. Using fromkeys() method to create a new dictionary
items = ['spices', 'vegetables', 'meat']
new_dict = dict.fromkeys(items, 0)
print("New dictionary using fromkeys method:", new_dict)

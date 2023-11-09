# List
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# Find the length of a list
list_length = len(my_list)
print("Length of the list:", list_length)

# Sort the list alphabetically
my_list.sort()
print("Sorted list:", my_list)

# Demonstrate the data type of your list
print("Data type of the list:", type(my_list))

# Tuple
my_tuple = (1, 2, 3, 4, 3, 2, 3, 4, 5, 3)
# Return the number of times a specific value repeatedly appears in the tuple
specific_value_count = my_tuple.count(3)
print("Count of specific value (3) in the tuple:", specific_value_count)

# Print the last item of the tuple
last_item = my_tuple[-1]
print("Last item of the tuple:", last_item)

# Demonstrate the data type of your tuple
print("Data type of the tuple:", type(my_tuple))

# Set
my_set = {1, 2, 3, 4, 5}
# Remove an item from the set
my_set.remove(3)
print("Set after removing an item:", my_set)

# Delete the set completely
del my_set
# Attempting to access my_set here would result in a NameError

# Demonstrate the data type of your set
# As my_set has been deleted, we'll recreate it for the demonstration
my_set = {1, 2, 3}
print("Data type of the set:", type(my_set))

# Dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# Get the value of a specific key element
value = my_dict['age']
print("Value of the key 'age':", value)

# Change the value of a specific item by referring to its key name
my_dict['age'] = 35
print("Updated dictionary:", my_dict)

# Demonstrate the data type of your dictionary
print("Data type of the dictionary:", type(my_dict))

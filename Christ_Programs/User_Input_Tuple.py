def take_tuple_input():
    input_string = input("Enter elements of the tuple separated by spaces: ")
    elements_list = input_string.split()
    user_tuple = tuple(elements_list)
    return user_tuple

# Test the take_tuple_input function
user_tuple = take_tuple_input()
print("User Tuple:", user_tuple)

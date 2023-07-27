def take_dict_input():
    user_dict = {}
    while True:
        key = input("Enter key (or type 'done' to finish): ")
        if key.lower() == 'done':
            break
        value = input(f"Enter value for '{key}': ")
        user_dict[key] = value

    return user_dict

# Test the take_dict_input function
user_dict = take_dict_input()
print("User Dictionary:", user_dict)

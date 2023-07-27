def create_user_dict():
    user_dict = {}
    while True:
        key = input("Enter key (or type 'done' to finish): ")
        if key.lower() == 'done':
            break
        value = input(f"Enter value for '{key}': ")
        user_dict[key] = value

    return user_dict

def main():
    # Step 1: Create a dictionary from user input
    user_dict = create_user_dict()

    # Step 2: Retrieve values from the dictionary
    while True:
        key_to_retrieve = input("Enter key to retrieve value (or type 'done' to exit): ")
        if key_to_retrieve.lower() == 'done':
            break

        value = user_dict.get(key_to_retrieve)
        if value is not None:
            print(f"Value for key '{key_to_retrieve}': {value}")
        else:
            print(f"Key '{key_to_retrieve}' not found in the dictionary.")

if __name__ == "__main__":
    main()


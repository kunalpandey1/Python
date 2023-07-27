def create(customer):
    name = input("Enter your Name: ")
    gender = input("Enter the gender: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")
    contact = input("Enter the contact number: ")
    order_purchase = input("Enter the order purchased: ")
    cost = float(input("Enter the cost of the product: "))
    purchase = (order_purchase, cost)
    customer.append({"name": name, "gender": gender, "email": email, "address": address, "contact": contact, "purchase": purchase})

def product(company):
    stock_item = int(input("Enter how many products are there in stock: "))
    for i in range(stock_item):
        prod = input("Enter the name of the product: ")
        cost = float(input("Enter the cost of the product: "))
        quantity = int(input("Enter the quantity of the product: "))
        company[prod] = {"cost": cost, "quantity": quantity}

def check_highest_price(company):
    if company:
        sorted_products = sorted(company.items(), key=lambda x: x[1]["cost"], reverse=True)
        print("Product with the highest price:")
        for product, details in sorted_products[:1]:
            print(f"{product} - Price: {details['cost']}")
    else:
        print("Product list is empty")

def print_products_over_5000(company, customer):
    print("Products worth more than 5000 purchased by customers:")
    for cust in customer:
        purchases = cust.get("purchase", [])
        for order_purchase, cost in purchases:
            if cost > 5000:
                product_name = order_purchase
                product_cost = company[product_name]["cost"]
                print(f"Customer: {cust['name']} - Product: {product_name}, Cost: {product_cost}")

if __name__ == "__main__":
    company = {}
    customer = []

    print("1 Create Customer details")
    print("2 Enter the product details")
    print("3 Find the product with the highest price")
    print("4 Print the products worth more than 5000 purchased by the customer")
    print("5 Exit the Program")

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            create(customer)
        elif choice == 2:
            product(company)
        elif choice == 3:
            check_highest_price(company)
        elif choice == 4:
            print_products_over_5000(company, customer)
        elif choice == 5:
            break
        else:
            print("Invalid choice, please try again.")

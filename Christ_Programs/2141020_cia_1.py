# A company has a list of products each with a name , price  and quantity in stock .
#  Prepare Seaprate list of clients/customers - Get their relevant details such as Name,Gender,Email address
#  (limit the number of characters) and contact , address, order purchase with cost - Use Relevant Datatypes

#  GET THE INPUT from the customer - use proper vaidation
# its mandatory to use list/tuple inside dictionary
# the company wants to find the product with the highest price and print 
# the price in sorted order
# print the products worth more than 5000 purchased by the customer with their details




def create(customer):
        name= str(input("Enter your Name"))
        gender= str(input("Enter the gender"))
        email=str(input("Enter the mail"))
        address=str(input("Enter the address"))
        contact=str(input("Enter the contact number"))
        order_purchase=str(input("Enter the order purchased"))
        cost=str(input("Enter the cost of the product"))
        purchase = (order_purchase,cost)
        user_input = customer.append((name,gender,email,address,contact,purchase))
        if customer is not None:
           if cost > 5000:
            print("Customer Details ",customer)
        return user_input

def product(company):
    stock_item = int(input("Enter how many products are their in the stock"))
    for i in range (0,stock_item):
       prod = str(input("Enter the name of the products"))
       cost = str(input("Enter the cost of the product"))
       quantity = str(input("Enter the quantity of the product"))
       company[quantity] = {"product":prod,"cost":cost}
       print("Product Details are ",company)
       return company

def check(company):
    if company is not None:
          sortt = sorted(company)
          print("Company highest product price is ",sortt[::-1])
    else:
            print("Product list is empty")
            return company
      


if __name__ == "__main__":
    company={}
    customer=[]

    print("1 Create Customer details")
    print("2 Enter the product details")
    print("3 Find the product with the highest price")
    print("4 Print the product worth more than 5000 purchased by the customer")
    print("5 Exit the Program")
    choice = int(input("Enter the choice from "))
    while choice!=5:
        if choice==1:
            user_input = create(customer)
        elif choice==2:
            product_input = product(company)
        elif choice==3:
            high = check(company,customer)
        elif choice==4:
            printing = printing(company,customer)

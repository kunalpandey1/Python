# *args       = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments




#  * -> unpacking operator


# 1 positional 2 Default 3 Keyword 4 arbitrary



#arbitrary arguments -> we don't know how many arguments user going to pass in



# ----- *ARGS Example 1 -----
 


def add(*nums):

   total = 0

   for num in nums:

       total += num

   return total



print(add(1, 2, 3, 4))



# ----- *ARGS Example 2 -----



def display_name(*args):

   print(f"Hello", end=" ")

   for arg in args:

       print(arg, end=" ")



display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")



# ----- **KWARGS -----

def print_address(**kwargs):

     #for value

    # for value in kwargs.values():

    #     print(value, end=" ")

    #for keys

    # for keys in kwargs.keys():
    #     print(keys)

     
     # for both

     for keys,value in kwargs.items():
        print(f"{keys} : {value}")


print_address(street="123 Fake St.",

              pobox="P.O Box 777",

              city="Detroit",

              state="MI",

              zip="54321")



# ----- EXERCISE -----

# make sure your keyword arguments is first and then your positional arguments  so first always will be args and then kwargs
 
def shipping_label(*args, **kwargs):

    for arg in args:

        print(arg, end=" ")

    print()



    if "apt" in kwargs: #if there is an apt key then print this line

        print(f"{kwargs.get('street')} {kwargs.get('apt')}")

    elif "pobox" in kwargs:

        print(f"{kwargs.get('street')}")

        print(f"{kwargs.get('pobox')}")

    else:

        print(f"{kwargs.get('street')}")



    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")



shipping_label("Dr.", "Spongebob", "Squarepants",

               street="123 Fake St.",

               pobox="PO box #1001",

               city="Detroit",

               state="MI",

               zip="54321")

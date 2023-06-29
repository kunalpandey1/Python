# Keyword Arguments = An argument preceded by an identifier helps with readability order of arguments doesn't matter


# 1 positional 2 Default 3 Keyword 4 arbitrary

# make sure positional arguments are first then key word arguments 


# ----- EXAMPLE 1 -----

def hello(greeting, title, first, last):

    print(f"{greeting} {title}{first} {last}")



hello("Hello", title="Mr.", last="John", first="James")



# ----- EXAMPLE 2 -----

for number in range(1, 11):

    print(number, end=" ")


#------------------------------------------------------------------------ 

print("1", "2", "3", "4", "5", sep="-") #separate function



# ----- EXERCISE -----

def get_phone(country, area, first, last):

    return f"{country}-{area}-{first}-{last}"



phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)

# In the code snippet you provided, the f is used as a prefix to create a formatted string, also known as an f-string, within the return statement.The purpose of an f-string is to embed expressions inside curly braces {} within a string and have them evaluated and replaced with their corresponding values at runtime.
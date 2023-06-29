# name = "bro code"

# print(len(name))
# print(name.find("o"))
# print(name.capitalize()) # it will capitalize only the first letter of bro to Bro and code to Code 
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("o","a"))
# print(name*3)



# -------------------------------

# STRING METHODS

# -------------------------------
# name = input("Enter your name: ")

# phone_number = input("Enter your phone #: ")



# length = len(name)

# index = name.find(" ")

# name = name.capitalize()

# name = name.upper()

# name = name.lower()

# result = name.isdigit()

# result = name.isalpha()

# result = phone_number.count(" ")

# phone_number = phone_number.replace("-", "")



# -------------------------------
#        EXERCISE
# -------------------------------

username = input("Enter a username: ")



if len(username) > 12:

   print("Your name can't be more than 12 characters")


      #If the find() method does not find a space in the username string, it returns -1. This means that the condition username.find(" ") == -1 evaluates to True when there are no spaces in the username string.However, the not keyword is used in front of the condition, which negates the result. 

elif not username.find(" ") == -1:

   print("Your username can't contain spaces")

elif not username.isalpha():

   print("Your username can't contain digits")

else:

   print(f"Welcome {username}!")


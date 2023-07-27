# If Statement

age = 25
if age >= 18:
    print("You are an adult.")


#For Loop

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)


#While Loop

count = 0
while count < 5:
    print("Count:", count)
    count += 1


#Conditional operator (Ternary Operator)
age = 17
is_adult = True if age >= 18 else False
print(is_adult)


#Switch statement (using dictionary):
def option_1():
    print("Option 1")

def option_2():
    print("Option 2")

options = {
    'a': option_1,
    'b': option_2,
}

user_choice = 'a'
options.get(user_choice, lambda: print("Invalid option."))()
#  the brackets () are necessary after the lambda function to invoke or call the function. In the given code, the lambda function is used as a default value in the options.get() method. If the user_choice key is not found in the options dictionary, the lambda function will be returned as the default value. In order to execute the lambda function, the brackets () are needed.

#Try-except block (exception handling):
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero.")


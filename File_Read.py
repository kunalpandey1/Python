try:
    with open('C:\\Users\\kunal\\Desktop\\python\\test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

finally:
    print(f"Ok File is Closed : {file.closed}")

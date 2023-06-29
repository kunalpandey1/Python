text = "This is some text\nHave a good one!\n"

with open('C:\\Users\\kunal\\Desktop\\python\\test.txt','w') as file:

    file.write(text)
    print(file.closed)
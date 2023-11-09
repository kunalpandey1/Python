f = open('abc.txt', 'w')
f.write("Something")
f.write("I am doing file operation")

#writing test.txt data to abc.txt file

f=open('test.txt', 'r')
f1=open('abc.txt', 'w')

for data in f:
    f1.write(data)
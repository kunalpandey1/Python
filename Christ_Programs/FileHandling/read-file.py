# r-> reading from a file
# w-> writing to a file
# a -> appending to a file
# r+-> reading and writing to a file
f=open('test.txt','r') # default is reading

# print(f.read())
# print(f.read(4)) # reading four characters from a file
print(f.readline(4),end='')
# print(f.readline()) #reading second line as readline is a pointer
# print(f.mode)

for data in f:
    print(data)

f.close()
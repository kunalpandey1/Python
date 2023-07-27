# Lists in python

# Creation:
# Indices start with 0
# Can hold values of different types
# Square Bracket

list1 = ['abc', 'def', 101, 201];
list2 = [1, 2, 3, 4, 5];
list3 = ["a", "b", "c", "d"]
print(list1,list2,list3)
print(type(list1[0]))
print(type(list3[0]))

# Accessing the values:

list1 = ['abc', 'def', 101, 201];
print( "list1[2]: ", list1[2])
list1[2]: 101

# Updating the values

list1 = ['abc', 'def', 101, 201];
print (list1)
print( "list1[2]: ", list1[2])
list1[2] = "QWERTY" # list allows to update the values as its mutable
print( "list1[2]: ", list1[2])
print(list1)
['abc', 'def', 101, 201]
list1[2]:101
list1[2]:"QWERTY"
['abc', 'def', 'QWERTY', 201]

# Delete an element

list1 = ['abc', 'def', 101, 201];
list2 = [1, 2, 3, 4, 5];
print(list1)
del list1[2]
print(list1)
del list1
#print(list1) #Deleted entire list(all elements)

list1 = ['abc', 'def', 101, 201]
list2 = [1, 2, 3, 4, 5]
print(len(list1))
list3 =list1 + list2
print(list3)
#for x in [1, 2, 3]: # demo to use list in for
# print(x)
4
['abc', 'def', 101, 201, 1, 2, 3, 4, 5]

# Exercise

# Try to implement operations like: Compare, length, max, min

# Tuple

# different ways of initializing a tuple
t1 = ('aaa', 'bbb', 1, 2);
t2 = (1, 2, 3, 4, 5 );
t3 = "a", "b", "c", "d"; # by default, its a tuple
t4 = ();
t5 = (5,);

# '
# aaa
# '
t1[0]

t30 =t1 + t2
print(t30)
print(t30[-1])
('aaa', 'bbb', 1, 2, 1, 2, 3, 4, 5)
5

del t30

# Try to declare tuples in a list

# Guess the output...

l = [(10,20,40), (40,50,60),(70,80,90)]
print(l[0])

(10, 20, 40)

print([t[:-1]+(100,) for t in l])
[(10, 20, 100), (40, 50, 100), (70, 80, 100)]
print(l)
[(10, 20, 40), (40, 50, 60), (70, 80, 90)]

l = [10,20,40]
print(l[:-1]) #all elements of the sequence but the last
print(l[:-1]+[100,] )
[10, 20]
[10, 20, 100]
t=(10,20,40)
print(t[:-1])
print(t[:-1]+(100,) )

print(l)

# Find out expressions for Compare, to find length, to find max, min

# Tuple to list and List to Tuple

#List to tuple
my_list = ['l1','l2','l3','l4','l5']
t = tuple(my_list)
print(my_list)
print(t)
['l1', 'l2', 'l3', 'l4', 'l5']
('l1', 'l2', 'l3', 'l4', 'l5')

#Tuple to list
my_tup = ('t1','t2','t3','t4','t5')

mylist1 = list(my_tup)
print(my_tup)
print(mylist1)
('t1', 't2', 't3', 't4', 't5')
['t1', 't2', 't3', 't4', 't5']

#Strings to list
str1 = "This is a python program"
li = list(str1.split(" "))
print(li)

['This', 'is', 'a', 'python', 'program']

#Reading a file
my_file = open("one.txt", "r")
content = my_file.read()
print(content)
# One Two Three Four

# File content into the list
content_list = content.split(" ")
my_file.close()
print(content_list)
['One', 'Two', 'Three', 'Four']

# Indexing and slicing

# declaring the string
str1 ="1234567890ABCDEF"
print(str1[1])
#2

# accessing the character of str1 at last index
print(str1[-1])
#F

# accessing the character of str1 at 5th index from the last
print(str1[-5])
#B

# accessing the character of str1 at 5th index from the last
print(str1[ 5])

print(str1[-5])
# accessing the character of str1 at 10th index from the last
print(str1[-10])

# slicing using indexing sequence
str1 ="1234567890ABCDEF"
print(str1[: 3])
print(str1[:])
print(str1[5:])
print(str1[1 : 7])
print(str1[1 : 7 : 2])
print(str1[-1 : -12 : -2])

# string[start : end : step]
# start : We provide the starting index.
# end : We provide the end index
# step : It is an optional argument that determines the increment between each index for
# slicing.

# Sets : A set is an unordered collection with no duplicate elements

subjects = {'python', 'networks', 'cloudcomputing', 'python', 'network', 'python_lab'}
# removed duplicates
print(subjects)
print('python' in subjects)
print('java' in subjects)

#set Operations
a = set('abracadabra')
b = set('alacazam')
# unique letters in a

print('Union', a.union(b))
print('Intersection', a.intersection(b))
print('Diff',b.difference(a))
print('sym',b.symmetric_difference(a))

print('a:',a)
print('a - b:',a - b) # letters in a but not in b
print('a | b:',a | b) # letters in a or b or both
print('a & b:',a & b) # letters in both a and b
print('a ^ b:',a ^ b) # letters in a or b but not both

# a: {0, 1, 5, 9}
# a - b: {0, 1}
# a | b: {0, 1, 5, 9}
# a & b: {9, 5}
# a ^ b: {0, 1}

a = {1, 5, 9, 0}
b = {5,9}
print(a.isdisjoint(b))
print(a.issubset(b))
print(a.issuperset(b))
print(b.difference(a))
c=set()
print(c)

z = {x for x in 'abracadabra' if x not in 'abc'}
print(z)
{'d', 'r'}

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)
# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)
# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)
# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# Dictionary
# 1. It holds Key:Value pair
# 2. Enclosed in {}
# 3. Key is unique and Values can be duplicated

# empty dictionary
my_dict1 = {}
print(my_dict1)
# dictionary with integer keys
my_dict2 = {1: 'apple', 2: 'ball'}
print(my_dict2)
# dictionary with mixed keys
my_dict3 = {'name': 'John', 1: [2, 4, 3]}
print(my_dict3['name'])
print(my_dict3[1])
# using dict()- constructor
my_dict4 = dict({1:'apple', 2:'ball'})
print(my_dict4)
# from sequence having each item as a pair
my_dict5 = dict([(1,'apple'), (2,'ball')])
print(my_dict5)

# Changing and adding Dictionary Elements
my_dict = {'name': 'Jack', 'age': 26}
# update value
my_dict['age'] = 27
print(my_dict)
# add item
my_dict['address'] = 'Downtown'
# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)

# Removing elements from a dictionary
# create a dictionary
squares = {11: 121, 4: 16, 2: 4, 3: 9, 5: 25}
# remove a particular item, returns its value
print(squares.pop(4)) # key 4
print(squares)
print(squares.popitem()) # pops last item
print(squares)
# remove all items
squares.clear()
# Output: {}
print(squares)
# delete the dictionary itself
del squares
# Throws Error
#print(squares)

# Nested Dictionary

# Creating a Nested Dictionary
Dict = {1: 'This ', 2: 'is a',
3:{'A' : 'Python', 'B' : 'Program'}}
print(Dict)
print(Dict.get(3))
print(Dict.get(2))
#print(Dict.get('three','notfound'))

print(Dict[1])
print(Dict[3]['A'])
Dict[3]['C'] ='ABC' #adding aka updating
print(Dict)

Dict.clear()
print(Dict)

del Dict[3]['C']
print(Dict)

del Dict[2]
print(Dict)



del Dict

#enumerate()
for i, v in enumerate(['tic', 'tac', 'toe']):

 print(i, v)

#zip()
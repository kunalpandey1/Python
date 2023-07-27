# dictionary =  a collection of {key:value} pairs

#  ordered and changeable. No duplicates

my_dict = {'key1': 1, 'key2': 'kunal'}
print(my_dict)

my_dict = dict(key1='value1', key2='value2')
print(my_dict)

my_dict = dict([('key1', 'value1'), ('key2', 'value2')])
print(my_dict)

keys = ['key1', 'key2']
values = ['value1', 'value2']
my_dict = dict(zip(keys, values))
print(my_dict)


capitals = {"USA": "Washington D.C.",

                    "India": "New Delhi",

                    "China": "Beijing",

                    "Russia": "Moscow"}


 
print(dir(capitals))

print(help(capitals))

print(capitals.get("Japan"))



if capitals.get("Russia"):

   print("That capital exists")

else:

   print("That capital doesn't exist")



capitals.update({"Germany": "Berlin"})

capitals.update({"USA": "Detroit"})

capitals.pop("China")

capitals.popitem()

capitals.clear()



keys = capitals.keys()

for key in capitals.keys():

  print(key)



values = capitals.values()

for value in capitals.values():

 print(value)



items = capitals.items()

for key, value in capitals.items():

   print(f"{key}: {value}")


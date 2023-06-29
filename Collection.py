#Collection = Single "Variable" used to store multiple values


#   List  = [] ordered and changeable. Duplicates OK

#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates

#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#List

fruits = ["apple","orange","banana","coconut"]
print(fruits)
print(fruits[0])
print(fruits[0:3]) #start ele : end ele
print(fruits[::2]) #every second element apple and banana
print(fruits[::-1]) #reverse order
print(len(fruits))
print("apple" in fruits)
print("pineapple" in fruits)
fruits[0] = "pineapple"
print(fruits)
fruits.append("Mango") #it will append at the end of the list
fruits.remove("apple")
fruits.insert(0,"Blueberry")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("apple"))
print(fruits.count("banana"))
for x in fruits:
    print(x)

    #or

for fruit in fruits:
    print(fruit)



# to list the different method available for collection you can do

print(dir(fruits)) 

#if you want description of these methods 

print(help(fruits))


#----------------------------------------------------------------------------------------------

#Set

fruits = {"apple","orange","banana","coconut"}

#we can't use the index of operator in set

fruits.pop() #remove whatever element is first in the set

#and all the operations shown above with list will be same for set 

#--------------------------------------------------------------------------------------------------

#tuple

fruits = ("apple","orange","banana","coconut")

#and all the operations shown above with list will be same for tuple


l=[(10,20,40),(40,50,60),(70,80,90)]
print(l[0])
print([t[:-1]+(100,)for t in l])
print(l[::-1])
reversed_inside_a_tuple = [t[::-1] for t in l[::-1]]
print(reversed_inside_a_tuple) # reverse each and every element
reversed_inside_a_tuple_2 = [t[::-1] for t in l]
print(reversed_inside_a_tuple_2) # reverse each and every element
print(l[:-1])
print(l[:+1])
print(l[0][:-1])


str1 = "This is a Python program"
li = list(str1.split(" "))
reversed_li = list(reversed(li))

print(reversed_li)
print(li)
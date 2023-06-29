# Convert a datatype of a value ton another data types

name = "Bro"
age = 21
gpa = 1.9
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student)) 

#Explicit Type Casting

age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

student = str(student)
print(student)

name = bool(name)
print(name)

#Implicit Type Casting
  
x=2
y=2.0

x=x/y
print(x)



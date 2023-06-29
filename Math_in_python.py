#arithmetic operators
# friends = 10
# friends = friends + 1
# friends+=1
# friends = friends - 2
# friends-=2
# friends = friends * 3
# friends = friends / 2
# friends/=2
# friends = friends ** 2
# friends **=2

# remainder = friends % 2

# print(remainder)
# print(friends)

#------------------------------------------

#built-in opeartor

# x=3.14
# y=4
# z=5

# result = round(x)
# result = abs(y)
# result = pow(4,3)
# result = max(x,y,z)
# result = min(x,y,z)

#Math Module

# import math

# x = 9

# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)

# print(result)

#--------------------------------------------------

# exercises 1

import math

radius = float(input("Enter the radius of a circle:"))

circumference = 2* math.pi * radius

print(f"The Circumference is :{round(circumference,2)}cm")


#exercise 2


import math

radius = float(input("Enter the radius of a circle:"))

area = math.pi * pow(radius,2)

print(f"The area of a circle is :{round(area,2)}cm^2")



#exercise 3

import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"SIde C = {c}")
#Class Variable is in  file Car.py
from Car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

#Car.wheels = 2  updating the wheels value it will affect both car_1 and car_2

print(car_1.wheels)
print(car_2.wheels)


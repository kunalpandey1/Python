from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete classes
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Dispatch function
def get_shape_info(shape):
    if isinstance(shape, Shape):
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
    else:
        raise TypeError("Invalid shape type")

# Usage of abstract class and dispatch
rect = Rectangle(5, 3)
circle = Circle(7)

get_shape_info(rect)
get_shape_info(circle)

# Try passing a non-shape object
# get_shape_info("Some string")

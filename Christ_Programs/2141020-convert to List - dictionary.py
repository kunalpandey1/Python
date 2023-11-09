class Duck:
    def quack(self):
        print('Quaack!')

    def walk(self):
        print('Walks like a duck')

D1 = Duck()
D1.quack()
D1.walk()

class Dog:
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

Dog1 = Dog()
print(Dog1.attr1)
Dog1.fun()

del Dog1  # Destroys object

# CREATING CLASS
class Employee:
    'NOTE: This class later will be used as a common base class for all employees - Document description'
    empCount = 0  # class var

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        # Function to display the number of employees
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        # Function to display employee details
        print("Name: ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        # Function to destroy class Employee objects
        class_name = self.__class__.__name__
        print(class_name, "object destroyed")
        Employee.empCount -= 1  # Decrementing object count
        print("Remaining objects of", class_name, Employee.empCount)

# CREATING OBJECTS
e1 = Employee("Zara", 2000)  # 1st object of Employee class
e2 = Employee("Amanni", 5000)  # 2nd object of Employee class
e3 = Employee("Amanni", 5000)  # 3rd object of Employee class
e1.displayEmployee()
e2.displayEmployee()
e3.displayEmployee()
print("Total Employee %d" % Employee.empCount)
del e1  # destructor
del e2  # destructor
del e3  # destructor

# ACCESSING BUILTIN CONTENT OF THE CLASS
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

# DESTRUCTOR
del e2
del e3

class Rectangle:
    # """SAMPLE EXAMPLE FOR DEMONSTRATING CLASSES & OBJECTS."""
    name = 'Rectangle'

    def __init__(self, length, breadth, unit_cost=1):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost

    def get_area(self):
        return self.length * self.breadth

    def calculate_cost(self):
        area = self.get_area()
        return area * self.unit_cost

# breadth = 120 units, length = 160 units, 1 sq unit cost = Rs 2000
print("name of the shape is", Rectangle.name)
r = Rectangle(160, 120, 2000)
print("The geometrical shape used here is:")
print("Area of Rectangle: %s sq units" % (r.get_area()))
print("cost of the land is:", r.calculate_cost())

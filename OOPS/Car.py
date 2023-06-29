class Car:

    wheels = 4 #class variable

    def __init__(self,make,model,year,color): #constructor
     self.make = make #instance variable
     self.model = model #instance variable
     self.year = year #instance variable
     self.color = color #instance variable
     

    def drive(self): #method and here self refes to object that is using that method
        print("This "+self.model+" is driving")


    def stop(self):
        print("This "+self.model+" is stopped")

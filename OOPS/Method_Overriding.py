class Animal:
    #overriden method

    def eat(self):

        print("This animal is eating")


class Rabbit(Animal):

    #overriding method

    def eat(self):

        print("This rabbit is eating a carrot")


rabbit = Rabbit()

rabbit.eat()
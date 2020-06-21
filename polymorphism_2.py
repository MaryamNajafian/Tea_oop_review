import random
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print (f"{self.name} is eating {food}")

class Dog(Animal):
    def __int__(self, name): # separate common functionality with more specific functionality
        # super(superclass,instance).method: get super class of Dog, and pass dog instance
        # super function give us access to inherit the parent class methods
        # here we are inheriting __init__ like any other method
        # if a class doesn't have an __init__ constructor,
        # Python automatically will check its parent class to see if it can find it
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Shi Tzu', 'Beagle', 'Mutt'])
    def fetch(self, item):
        print(f"{self.name} goes after the {item}")
    def show_affection(self):
        print(f"{self.name} wags tail")

class Cat(Animal):
    def swatstring(self):
        print(f"{self.name} shreds the string")
    def show_affection(self):
        print(f"{self.name} purrs")


r = Dog('Rover')
f = Cat('Fluffy')

r.fetch('paper')
f.swatstring()
r.eat('dog food')
f.eat('cat food')
f.swatstring()

for a in (Dog('Rover'), Cat('Fluffy'), Cat('Precious'), Dog('Scout')):
    a.show_affection()
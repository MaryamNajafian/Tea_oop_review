class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print (f"{self.name} is eating {food}")

class Dog(Animal):
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
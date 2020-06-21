"""
ATTRIBUTE ENCAPSULATION:
@property is a decorator that designates an instance attribute as encapsulatable through methods
Getting, Setting, Deleting methods can be defined, called automatically when a user accesses the attribute

@property should not encapsulate  expensive operations, because attribute  setting looks cheap
"""

class GetSet:
    def __init__(self,value):
        self.attrval = value

    @property
    def var(self):
        print("getting the var attribute")
        return self.attrval

    @var.setter
    def var(self,value):
        print("setting the var attribute")
        self.attrval = value

    @var.deleter
    def var(self):
        print("deleting the var attribute")
        self.attrval = None

me = GetSet(5)
me.var = 1000
print(me.var)
del(me.var)
print(me.var)
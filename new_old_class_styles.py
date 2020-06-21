"""
New-Style classes inherit from `object`
can be constructed with default attributes from `metaclass` constructors
Allow the subclassing of built-ins
Allow the use of `slots` to define instance attributes
Use method resolution order 'C3' MRO
support `descriptors`
Are the only style of class in Python 3
"""
class OldClass():
    pass

class NewClass(object):
    pass

class MyClass:
    pass

oc = OldClass()
nc = NewClass()
mc = MyClass()

print(type(oc))
print(type(nc))
print(type(mc))

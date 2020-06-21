
"""
Method overloading:
when working in child class we can choose to implement parent class methods in different ways:
    * Inherit: simply use parent class's defined method
    * Override/overload: provide child's own version of a method
    * Extend: do work in addition to that in parent's method
    * Provide: implement abstract method that parent requires
"""
import abc

class GetSetParent: #this class inherits from object
    __metaclass__ = abc.ABCMeta # it shows GetterSetParent is an Abstract base class, and hence can't be instantiated separately

    def __init__(self,value):
        self.val = 0

    def set_val(self,value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod # it shows showdoc is an Abstract method
    def showdoc(self): # abstract methods do nothing and only have a return
        return


class GetSetInt(GetSetParent): # this class inherits from GetSetParent
    def set_val(self, value):
        if not isinstance(value,int):
            value = 0
        # Specializing: calling the parent; It looks for superclass GetSetInt, calls setval method, and passes the instance as an argument
        super(GetSetInt,self).set_val(value)
    def showdoc(self):
        # shows instance ID
        print(f"GetSetInt object{id(self)}, only accepts integer values")

class GetSetList(GetSetParent): # this class inherits from GetSetParent
    def __init__(self,value=0):
        self.vallist = [value]
    def get_val(self):
        return self.vallist[-1]
    def get_vals(self):
        return  self.vallist
    def set_val(self, value):
        self.vallist.append(value)
    def showdoc(self):
        print(f"GetSetList object length is {len(self.vallist)}.")

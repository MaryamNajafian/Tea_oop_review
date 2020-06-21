"""
Abstract class: it is a kind of "model" for other classes to be defined.
                it is not designed to construct instances, but can be subclassed by regular classes
                it can define interface/methods that must be implemented by its subclasses
"""
import abc


class GetterSetter:
    __metaclass__ = abc.ABCMeta  # it shows GetterSetter is defined as an Abstract base class

    @abc.abstractmethod
    def set_val(self, input):
        """ Set a value in the instance """
        return

    @abc.abstractmethod
    def get_val(self):
        """ Get and return a value from the instance"""
        return


class MyClass1(GetterSetter):

    def set_val(self, input):
        self.val = input

    def get_val(self):
        return self.val


class MyClass2(GetterSetter):

    def set_val(self, input):
        self.val = input

    def get_val(self):
        return self.val

    def multiply(self):
        return self.val

x = MyClass1()
x.set_val(3)
print("subclass of abstract class can be instantiated:",x.get_val())

xx = MyClass2()
xx.set_val(33)
print("subclass of abstract class can be instantiated:",xx.get_val())

y = GetterSetter()
y.set_val(3)
print("can't instantiate the abstract class GetterSetter:",y.get_val())


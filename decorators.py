"""
instance methods: when the instances are bound to the methods. Instances work with the methods.
                 e.g. method(self) : is an instance method, because it gets the instance as the first argument

class methods:  if we apply the class method decorator to a method we can cause that method to pass the class automatically instead of the instance
                decorator is a special function that can modify functions
                class method decorator: @classmethod

static methods: a static method is just a utility class and it works  with the class code but its is neither a class nor an instance method
                if the method is intended to just be a utility method, it doesn't need the instance to work
                static method decorator: @staticmethod
"""

class InstanceCounter:
    count = 0
    def __init__(self,val): # instance method
        self.val = self.filterint(val)
        InstanceCounter.count += 1

    def set_val(self,newval): # instance method
        self.val = newval

    def get_val(self):  # instance method
        return self.val

    def get_count(self):  # instance method
        return InstanceCounter.count


    @classmethod # method decorator
    def get_count2(clas):      # class method
        return clas.count

    @staticmethod # static method decorator
    # to make sure the argument passed to the constructor is an integer
    def filterint(value): # self is not passed and value is  passed directly to the static method
        if not isinstance(value, int):
            return 0
        else:
            return value


a = InstanceCounter(5)
b = InstanceCounter(55)
c = InstanceCounter(555)
d = InstanceCounter('5555')

print(f'calling class method directly (no instance needed):{InstanceCounter.get_count2()}')
print(f"calling class method from the class instance:{a.get_count2()}")
print(f"calling instance method (can't be called from class directly):{a.get_count()}")

for obj in (a,b,c):
    print(f"val of obj: {obj.get_val()}")
    print(f"count {obj.get_count()}")
    print(f"object value is: {obj.val}")

for obj in (a,b):
    print(f"val of obj: {obj.get_val()}")
    print(f"count {obj.get_count2()}")
    print(f"object value is: {obj.val}")
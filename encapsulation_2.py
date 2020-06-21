class MyClass:
    classy = 'class attribute'
    def __init__(self,variable):
        print('calling __init__')
        try:
            variable = int(variable)
        except ValueError:
            variable = 0
        self.var = variable

    def set_val(self,value):
        self.var = value * value

    def get_val(self):
        return self.var

    def increment_val(self):
        self.var = self.var + 1

a = MyClass(10)
print(a.var)

a.set_val(100)
print(a.get_val())

a.set_val(1000)

a.val = 10000
print(a.get_val())

# GIVES ERROR IN NEXT STAGE
# a.val = '10000'
# print(a.get_val())

a.increment_val()
print(a.val)
print(a.get_val())

print(a.classy)

a.classy = 'instance attribute'
print(a.classy)


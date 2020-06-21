class MyClass:
    var = 10

    def print_val(self):
        print("Hi")

    #ENCAPSULATION: to insure integrity of the data going in and reject any data that isn't working
    def set_val(self,val):
       #To ensure the value in the val is always an integer
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def get_val(self):
        return self.val

    def increment_val(self):
        self.val = self.val + 1

a = MyClass()
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

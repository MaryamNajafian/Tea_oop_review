"""
Implementing Python's core syntax:

* Core syntax features translate to "magic" method calls
* Link: http://www.rafekettler.com/magicmethods.html
* We want our classes to respond to:
    * operators like `+, - , *, /, in`, etc
        * var.__add__(var2) ~    var1 + var 2
        * 'abc' in var      ~    var.__contains__('abc')
        * var == 'abc'      ~    var.__eq__('abc')
        * var[1]            ~    var.__getitem__(1)
        * var[1:3]          ~    var.__getslice__(1,3)
        * len(var)          ~    var.__len__()
        * print(var)        ~    var.__repr__()

    * builtin functions `len() and str() `
    * looping, slices, etc
"""

class SumList:
    def __init__(self,this_list):
        self.mylist = this_list

    def __add__(self,other): # cc.__add__(dd): self.mylist.__add__(other.mylist) : self.mylist + other.mylist
        new_list = [x+y for x,y in zip(self.mylist,other.mylist)]
        return SumList(new_list) # we receive a SumList Object which we can print

    def __repr__(self):
        return str(self.mylist)

cc = SumList([1,2,3,4,5])
dd = SumList([100,200, 300, 400, 500])
ee = cc + dd # cc.__add__(dd)

print(ee) # [101, 202, 303, 404, 505]
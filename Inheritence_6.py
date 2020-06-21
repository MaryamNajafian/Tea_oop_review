"""
Subclassing built-ins:
Inheriting from python built-in objects: Python lets our classes inherit from builtin classes. We can take advantage of core
builtin functionality, but customize selected operations.

"""


# %%
class MyDict(dict):# inherit from dict
    pass


dd = MyDict()
dd['a'] = 5
dd['b'] = 6

for key in dd.keys():
    print(f"{key}={dd[key]}")

dd = MyDict()
dd['a'] = 5
dd['b'] = 6
for key in dd.keys():
    print(f"{key}={dd[key]}")


# %%

class MyDict2(dict):# inherit from dict
    def __setitem__(self, key, val):
        print("setting kkey-value pairs.")
        dict.__setitem__(self, key, val)


dd = MyDict2()
dd['a'] = 5
dd['b'] = 6
for key in dd.keys():
    print(f"{key}={dd[key]}")


# %%
# MyList inherits from "list" object but indexes from 1 instead of 0! so x[index_i] reflects x[index_i-1]

class MyList(list):# inherit from list
    def __getitem__(self, index): # it will be used when calling: var_in_list[index], e.g. x[1]
        if index == 0: raise IndexError
        if index > 0: index = index - 1
        return list.__getitem__(self, index) #calling getitem from object 'list' with the new index
                                            # this  method is cakled when we access a value with subscript (x[1])

    def __setitem__(self, index, val): # it will be used when appending list_name.append('value at index i')
        if index == 0: raise IndexError
        if index > 0: index = index - 1
        list.__setitem__(self, index, val)

x = MyList(['a','b','c'])   # __init__() inherited from builtin list
print(x)                    #__repr__() inherited from builin list
x.append('spam')            #append() inherited from builin list

print(x[1])                 # index 1, but reflects 0
print(x[4])                 # index 4, but reflects 3

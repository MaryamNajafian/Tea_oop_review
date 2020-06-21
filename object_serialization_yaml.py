"""
Serialization means persist storage to disk
storing data between ex
Relational storage writes data to tables
Object-based storage stores objects as they are used in code (Object databases)
Object-relational mappings can mediate between the two
YAML serializes python objects like Pickle and JSON: sudo pip install pyyaml
YAML uses white space to separate elements
key: value1
key2: value2
key3:
- listelement1
- listelement2
- listelement3
- listelement4

"""
import yaml
import json

mydict = {'a':1, 'b':2, 'c':3}
mylist = [1,2,3,4,5]
mytuple = ('x','y','z')
mycomplexmix = (
    [1,2,3,4,5],
    {'a':1,'b':2,'c':3},
    [
        {'x':90, 'y': 99},
        3,
        4
    ],
    {'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9]}
)

loaded_yaml = yaml.dump(mydict, default_flow_style=False)
print(loaded_yaml)
print(yaml.dump(mylist, default_flow_style=False))
print(yaml.dump(mytuple, default_flow_style=False))
print(yaml.dump(mycomplexmix, default_flow_style=False))
#%%
with open("app.yaml") as f:
    struct = yaml.load(f)

print(struct)
print(type(struct))

# more readable

print(json.dumps(struct,indent = 4, separators=(',',': ')))

#%%

import yaml
class MyClass:
    classvar = 10
    def __init__(self,val):
        self.val = val
    def increment(self):
        self.val += 1

x = MyClass(5)
x.increment()
x.increment()

with open('obj.yaml','w') as f:
    yaml.dump(x,f)

with open('obj.yaml') as f:
    inst = yaml.load(f)
    # to limit the load to lists, dict etc and to avoid malicious code
    inst = yaml.safe_load(f)

print(inst.val)

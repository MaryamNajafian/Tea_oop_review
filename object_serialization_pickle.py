"""
Serialization means persist storage to disk
storing data between ex
Relational storage writes data to tables
Object-based storage stores objects as they are used in code (Object databases)
Object-relational mappings can mediate between the two
"""
import pickle
mylist = ['a','b','c','d']

with open('datafile.txt', 'w') as f:
    pickle.dump(mylist,f)

with open('config.txt') as f:
    unpickledlist = pickle.load(f)
print(unpickledlist)

mylist2 = ['a','b',1,2,3]
x = pickle.dumps(mylist2)
var = pickle.loads(x)
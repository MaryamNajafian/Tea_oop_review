"""
Serialization means persist storage to disk
storing data between ex
Relational storage writes data to tables
Object-based storage stores objects as they are used in code (Object databases)
Object-relational mappings can mediate between the two
Unlike pickle, json is readable by humans and uses "" and , to separate
"""
import json
with open('backup_config.json') as fh:
    conf = json.load(fh)

conf['newinputs'] = 5.0005

with open('backup_config.json','w') as fh:
    json.dump(conf,fh)

# more readable
with open('backup_config.json','w') as fh:
    json.dump(conf,fh, indent = 4, separators=(',',': '))

print(conf)
print(type(conf))

#%%
import json
x_dict = {'a':[1,2,3], 'c':[7,8,9], 'b':[4,5,6]}
x = json.dumps(x_dict)
mystruct = json.loads(x)
for key, val in mystruct.items():
    print(key,val)


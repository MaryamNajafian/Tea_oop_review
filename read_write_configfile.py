"""
Read a config file with key,value format and create a dictionary out of the values
When we are writing to the dictionary, we are actually writing to the file
for this we should create a configdict class that inherits from the dictionary
"""
import os
class ConfigDict(dict):
    def __init__(self,filename):
        self._filename = filename
        if os.path.isfile(self._filename):
            with open(self._filename) as fh:
                for line in fh:
                    line = line.rstrip()
                    key,value=line.split('=',1) # split the value on the first `=` sign
                    dict.__setitem__(self,key,value)

    def __setitem__(self, key, value):
        dict.__setitem__(self,key,value)
        with open(self._filename,'w') as fh:
            for key, val in self.items():
                fh.write(f"{key}={val}")

cc = ConfigDict('config.txt')
cc['key'] = 'value' # calls __setitem__
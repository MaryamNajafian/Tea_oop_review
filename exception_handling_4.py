"""
Define our own costume exception classes for the configclass
Read a config file with key,value format and create a dictionary out of the values
When we are writing to the dictionary, we are actually writing to the file
for this we should create a configdict class that inherits from the dictionary
raise an error if the key doesn't exist
"""

import os
def ConfigKeyError(Exception):
    def __init__(self,this, key):
        self.key = key
        self.keys = this.keys()
    def __str__(self):
        return f"key {self.key} not found. Available keys: {self.keys}"


class ConfigDict(dict):
    def __init__(self,filename):
        self._filename = filename
        if not os.path.isfile(self._filename):
            try:
                open(self._filename,'w').close()
            except IOEError:
                raise IOError('arg to ConfigDict must be valid pathname')
            with open(self._filename) as fh:
                for line in fh:
                    line = line.rstrip()
                    key,value=line.split('=',1) # split the value on the first `=` sign
                    dict.__setitem__(self,key,value)

    def __getitem__(self, key):
        if not key in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self,key)

    def __setitem__(self, key, value):
        dict.__setitem__(self,key,value)
        with open(self._filename,'w') as fh:
            for key, val in self.items():
                fh.write(f"{key}={val}")

    def __setitem__(self, key, value):
        dict.__setitem__(self,key,value)
        with open(self._filename,'w') as fh:
            for key, val in self.items():
                fh.write(f"{key}={val}")




cc = ConfigDict('config.txt')
cc['key'] = 'value' # calls __setitem__
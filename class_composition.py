"""
Class composition vs Inheritance

* Inheritance can lead to unnecessary restrictions as it establishes dependencies between parent and child class, and one change in one part of the code can break it
* Decomposition choses independent classes that can work together and are not related
    * Elements are decoupled: elenments are interactive and independent
    * The idea behind composition is to use 2+ classes that are not related by inheritance together
    * When there are fewer dependencies, there are less chances of changes in one part of the code breaking the code

"""
import random
from io import StringIO
""" 
# file builtin class: writes to files
# StringIO builtin class: writes to string buffer
# string buffer is just a string and it is an object that we can write to as if it was a file
# This code is an example of modularity: doesn't matter what object we pass to the WriteMyStuff,
  it takes whatever it receives and apply write on it
# different objects  are aware of each other's interface but they are decoupled and don't rely on each other
"""
class WriteMyStuff:
    def __init__(self,writer):
        self.writer = writer

    def write(self):
        write_text = "Hey!"
        self.writer.write(write_text)

file = open('test.txt','w')
w1 = WriteMyStuff(file)
w1.write()
file.close()

file2 = StringIO()
w2 = WriteMyStuff(file2)
w2.write()

print(f"file object: {open('test.txt','r').read()}")
print(f"StringIO object: {file2.getvalue()}")


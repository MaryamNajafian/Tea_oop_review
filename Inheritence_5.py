import abc
from datetime import datetime

class WriteFile:
    # we set WriteFile as an abstract class cause we want the other 2 classes to implement it
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return

    def __init__(self,filename):
        self.filename = filename

    def write_line(self,text):
        file = open(self.filename,'a')
        file.write(text + '\n')
        file.close

class DelimFile(WriteFile):
    def __init__(self,filename,delim):
        # calling the parent class of DelimFile class
        super(DelimFile,self).__init__(filename)
        self.delim = delim

    def write(self, this_list):
        line = self.delim.join(this_list)
        self.write_line(line)

class LogFile(WriteFile):
    def write(self, this_line):
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M')
        self.write_line(f'{date_str}    {this_line}')
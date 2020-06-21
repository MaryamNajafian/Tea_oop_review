
class Date: #inherits from the 'object' class
    def get_data(self):
        return '0000-00-00'

class Time (Date): # inherits from `Data` class
    def get_time(self):
        return '00:00:00'

dt = Date()
print(dt.get_data())

tm = Time()
print(tm.get_time())
print(tm.get_data())
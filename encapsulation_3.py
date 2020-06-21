class InstanceCounter:
    count = 0
    def __init__(self,val):
        self.val = val
        InstanceCounter.count += 1
        self.inner_list = []

    def set_val(self,newvalue):
        self.val = newvalue
        self.innerlist.append(newvalue)

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(3)
b = InstanceCounter(33)
c = InstanceCounter(333)
d = InstanceCounter(333)

for obj in (a,b,c):
    print(f"val of obj {obj.get_val()}")
    print(f"count: {obj.get_count()}")
    print(f"count from instance: {obj.count}")
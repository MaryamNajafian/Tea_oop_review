"""
* module name: all_lower_case
* Class names and exception names: CameCase
* Global and locals: all_lower_case
    * "Public" attributes/variables: intended to be used by the importer of the module or user of the class
    * "Private" attributes/variables `_single_leading_underscore`: if for internal use by the module or class
    * "Private" attributes: `__double_leading_underscore` : if for internal use (should not be subclassed)
    * "Magic" attributes: `__double_underscores__` (use them dont create them!)
* Functions and methods: all_lower_case
* Constants ALL_CAPS
"""
class GetSet:
    instance_count = 0
    __mangled_name = 'no privacy!'

    def __init__(self,value):
        self._attrval = value
        GetSet.instance_count += 1

    @property
    def var(self):
        print("getting the var attribute")
        return self._attrval

    @var.setter
    def var(self, value):
        print("setting the var attribute")
        self._attrval = value

    @var.deleter
    def var(self):
        print("deleting the var attribute")
        self._attrval = None

me = GetSet(5)
me.var = 1000
print(me.var)
del (me.var)
print(me.var)
print(me._attrval)
print("going out of our way to access this private attribute")
print(me._GetSet__mangled_name)
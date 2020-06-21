### OOP: Three Pillars

* Encapsulation: In Python Encapsulation is the process of wrapping up variables and methods into a single entity, such as class.
* Inheritance: It allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.
    * Multiple inheritance: Python method resolution order uses a depth-first search for inheritence of an attribute
    * Multiple inheritance (diamond shaped pattern) 
    * Inheriting from python built-in objects: Python lets our classes inherit from builtin classes. We can take advantage of core
builtin functionality, but customize selected operations.
* Polymorphism: It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.


### Object Attribute Lookup Hierarchy

* First - The instance
* Second - The class
* Third - Any class from which this class inherits

### Tricks

* To learn all methods of a class: `print(dir(ClassName))`
* To learn multiple inheritance order `print(ClassName.mro())`

### Methods
classes can contain class  methods, instance methods and static methods

* Instance methods: when the instances are bound to the methods. Instances work with the methods.
                 e.g. method(self) : is an instance method, because it gets the instance as the first argument

* Class methods:  if we apply the class method decorator to a method we can cause that method to pass the class automatically instead of the instance
                decorator is a special function that can modify functions
                class method decorator: @classmethod

* Static methods: a static method is just a utility class and it works  with the class code but its is neither a class nor an instance method
                if the method is intended to just be a utility method, it doesn't need the instance to work
                static method decorator: @staticmethod
                
### Classes
* Abstract class: it is a blueprint for how subclasses should be designed
                * it is not designed to construct instances, but can be subclassed by regular classes
                * it can define interface/methods that must be implemented by its subclasses

* Regular classes: it is a blueprint for instances
                * A class defines the attributes that that would be set in instances
                as well as defining attributes that the instance can access through class attributes
                
                
### Method overloading:
When working with a child class we can choose to use the parent class methods in different ways:

* Inherit: use inheritance to avois=d code duplication by using parent class's defined method. General functionality goes to the parent class and specific behaviour to each child class
* Override/overload: provide child's own version of a method
* Extend: do work in addition to that in parent's method
* Provide: implement abstract method that parent requires

### Class composition vs Inheritance
* Inheritance can lead to unnecessary restrictions as it establishes dependencies between parent and child class, and one change in one part of the code can break it 
* Decomposition chooses independent classes that can work together and are not related
    * Elements are decoupled: elenments are interactive and independent 
    * The idea behind composition is to use 2+ classes that are not related by inheritance together 
    * When there are fewer dependencies, there are less chances of changes in one part of the code breaking the code
    * Objects are modular: different objects are aware of each other's interface but they are decoupled and don't rely on each other in a hierarchy
    
    
### Implementing Python's core syntax 

* Core syntax features translate to "magic" method calls
* Link: http://www.rafekettler.com/magicmethods.html
* We want our classes to respond to: 
  operators like `+, - , *, /, in` etc; builtin functions `len() and str() `; looping, slices, etc

    * var.__add__(var2) ~    var1 + var 2
    * 'abc' in var      ~    var.__contains__('abc')
    * var == 'abc'      ~    var.__eq__('abc')
    * var[1]            ~    var.__getitem__(1)
    * var[1:3]          ~    var.__getslice__(1,3)
    * len(var)          ~    var.__len__()
    * print(var)        ~    var.__repr__()
    
### PEP 8 -- variable naming

* module name: all_lower_case
* Class names and exception names: CameCase
* Global and locals: all_lower_case
    * "Public" attributes/variables: intended to be used by the importer of the module or user of the class
    * "Private" attributes/variables `_single_leading_underscore`: if for internal use by the module or class 
    * "Private" attributes: `__double_leading_underscore` : if for internal use (should not be subclassed)
    * "Magic" attributes: `__double_underscores__` (use them dont create them!)
* Functions and methods: all_lower_case
* Constants ALL_CAPS

### Object Serialization
* serialization means persist storage to disk
* storing data between ex
* Relational storage writes data to tables
* Object-based storage stores objects as they are used in code (Object databases)
* Object-relational mappings can mediate between the two




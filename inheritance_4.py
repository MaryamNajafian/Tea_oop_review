
""" Multiple inheritance """
class A:
    def dothis(self):
        print("doing this in A")

class B(A):
    pass

class BB(A):
    def dothis(self):
        print("doing this in BB")


class C:
    def dothis(self):
        print("doing this in C")


class D(B,C):
    pass

class E(B,BB):
    pass


print(D.mro())
print(E.mro())

d_instance = D()
d_instance.dothis()

"""
Explanation: 
Multiple inheritance: Depth first search: D>B>A>C
     D
  |     |
  B     C
  |
  A


Multiple inheritance: Diamond resolution: Depth first search :
earlier appearances of repetition are removed from method resolution order : D>B>A>BB>A --> D>B>BB>A

     D
  |     |
  B     BB
  |     |
     A
"""

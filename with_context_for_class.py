"""
`__With__` Some objects need to "clean up" when done!
    * File object needs to close()
    * A network connection may need to close
    * A data intensive operation may need to `del` the data
    * __with__ provides a block that ""cleans up" when exited
    * `with` can handle and catch an exception within a block!
    * `with` can also execute code when entered
    """
#%%
class MyClass:
    def __enter__(self):
        print("We have entered `with`")
        return self
    def __exit__(self,type, value, traceback):
        # if an exception happens these values are set: type, value,traceback
        print("We are leaving `with`")
    def sayhi(self):
        print(f"hi, instance {id(self)}")

with MyClass() as cc:
    cc.sayhi()

print("after the `with` block")

#%%
class MyClass:
    def __enter__(self):
        print("We have entered `with`")
        return self
    def __exit__(self, type, value, traceback):
        #if an exception happens these values are set: type, value,traceback
        print(f"error type {type}")
        print(f"error value {value}")
        print(f"error type {traceback}")
        print("We are leaving `with`")
    def sayhi(self):
        print(f"hi, instance {id(self)}")

with MyClass() as cc:
    cc.sayhi()
    print("Creat a 'ZeroDivisionError'! \n")
    5/0

print("after the `with` block")
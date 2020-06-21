"""
Exceptions: every error that python encounters is identified by a `type`
Define our own costume exception classes
"""
class MyError(Exception):
    def __init__(self, *args):
        print("calling init")
        if args:
            self.message = args[0]
        else:
            self.message = ''
    def __str__(self):
        print("calling str")
        if self.message:
            return f"here is MyError exception with a message: {self.message}"
        else:
            return "here is a MyError exception"

raise MyError
raise MyError("Seems like we have a problem!")



"""
Exceptions: every error that python encounters is identified by a `type`
identify exceptions (errors):
trapping exceptions with try/except:
raising exceptions with raise:
defining custom exception class:
"""
import sys
mydict = {'a':1, 'b':2,  'c':3, 'd':4}
key = input('please input a key: ')

try:
    print("testing for error")
    print(f'the value for {key} is {mydict[key]}') # as soon as the error happens in this line the except block will execute
    print("everything is ok!")
except KeyError:
    print("trapped error")
    print(f"the key {key} doesn't exist, continuing... ")

except IndexError:
    print("trapped error, exiting...")
    sys.exit()

except (IndexError,KeyError):
    exit("please enter an int")

print("Thanks for int")
print("To be continued ...")
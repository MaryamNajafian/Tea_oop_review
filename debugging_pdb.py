
"""

type `c` for `continue`: keep you in current context and wont enter any functions
type 's' for step: steps into function and run line-line
type 'n' for next: next line
type 'l' for showing you where you are in the code
type 'h' list of functions available
"""
import pdb
def doubleval(argsum,val):
    argsum=0
    newval = argsum+val
    return newval
pdb.set_trace()

values = [1,2,3,4,5]
mysum = 0
totall = 0

for val in values:
    mysum = mysum + val
    totall = totall + doubleval(mysum,val)
    #pdb.set_trace()

print(mysum)
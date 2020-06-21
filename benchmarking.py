"""
Benchmarking with TIMEIT
benchmarking means comparing two code snippets to see which executes faster
time tests should be run multiple times
tests should consider the context in which they will run
"""

# import timeit
# a = timeit.timeit(stmt="mydict['c']",setup="mydict = {'a':5, 'b':6, 'c':7}", number=100000)
# b = timeit.timeit(stmt="mydict.get('c')",setup="mydict = {'a':5, 'b':6, 'c':7}", number=100000)
# print(f"test a: {a}")
# print(f"test b: {b}")
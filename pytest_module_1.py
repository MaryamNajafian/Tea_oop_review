"""
"sudo pip instal pytest"

Python tests are Python programs that test other  Python program
py.test: looks for scripts fuctions/methods called "test_"
After calling function or method, "assert" something is true
"with pytest.raises()" to assert that an exception is raised
"setup_class()" method to test prep
"teardown_class()" method to clean up after tests
"""

import pytest_module_1
import pytest
import os
import sys


def doubleit(x):
    var = x * 2
    return var


# if we execute this code direct we will exeute this block of code
# However if we import the program from another script this block of code won't get executed
if __name__ == '__main__':
    input_val = sys.argv[1]
    doubled_val = doubleit(input_val)
    print(f'the value of {input_val} is {doubled_val}')


def test_doubleit():
    assert pytest_module_1.doubleit(10) == 20


def test_doubleit_type():
    with pytest.raises(TypeError):
        pytest_module_1.doubleit('hello')

"""
"sudo pip install pytest"

Python tests are Python programs that test other  Python program
py.test: looks for scripts fuctions/methods called "test_"
After calling function or method, "assert" something is true
"with pytest.raises()" to assert that an exception is raised
"setup_class()" method to test prep
"teardown_class()" method to clean up after tests

    # python pytest requires programs starting with "test_xxxxx"
    # we set up a test class with a setup and teardown methods
    # if we insert a True statement into "assert", nothing happens
    # if we insert a False statement into "assert", we get sn "assertion" error

"""

import pytest_module_2
import pytest
import os
import sys
import shutil

def doubleit(x):
    var = x * 2
    return var

def doublelines(filename):
    with open(filename) as f:
        newlist = [str(doubleit(int(val))) for val in f]
    with open(filename, 'w') as f:
        f.write('\n'.join(newlist))

if __name__ == '__main__':

    input_val = sys.argv[1]
    doubled_val = doubleit(input_val)
    print(f'the value of {input_val} is {doubled_val}')

class TestDoubleIt:

    numbers_file_template = 'testnums_template.txt'
    numbers_file_tensor = 'testnums.txt'

    def setup_class(self):
        shutil.copy(TestDoubleIt.numbers_file_template, TestDoubleIt.numbers_file_tensor)

    def test_filename(self):
        assert not os.path.isfile(TestDoubleIt.numbers_file_tensor)
        assert os.path.isfile(TestDoubleIt.numbers_file_template)

    def teardown_class(self):
        os.remove(TestDoubleIt.numbers_file_tensor)

    def test_doublelines(self):
        pytest_module_2.doublelines(TestDoubleIt.numbers_file_tensor)
        old_vals = [int(line) for line in open(TestDoubleIt.numbers_file_template)]
        new_vals = [int(line) for line in open(TestDoubleIt.numbers_file_tensor)]
        for old_val, new_val in zip(old_vals,new_vals):
            assert int(new_val) == int(old_val) * 2


    def test_doubleit_value(self):
        assert pytest_module_2.doubleit(10) == 20


    def test_doubleit_type(self):
        with pytest.raises(TypeError):
            pytest_module_2.doubleit('hello')
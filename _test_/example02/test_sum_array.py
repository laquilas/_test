import pytest
import sys
sys.path.append("\\".join(__file__[:__file__.find('_test_')-1].split("\\")))

from example02.function02 import sum_array


def test_foo_bar1():
   array = [1,2,3,4,5,6]
   assert sum_array(array) == 21

def test_foo_bar2():
   array = [1,7,3,4,5,6]
   assert sum_array(array) == 26

def test_foo_bar3():
   array = [1,2,3,4,5,6]
   assert sum_array(array) != 22

def test_foo_bar4():
   array = [10,2,3,4,5,6]
   assert sum_array(array) != 1


if __name__ == "__main__":
    test_foo_bar1()